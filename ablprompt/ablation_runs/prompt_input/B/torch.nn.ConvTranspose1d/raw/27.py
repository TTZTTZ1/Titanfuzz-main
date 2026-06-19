import torch
import torch.nn as nn

# Define a model with ConvTranspose1d
class UpSampleModel(nn.Module):
    def __init__(self):
        super(UpSampleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=32, out_channels=16, kernel_size=5, stride=2, padding=1, output_padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and some dummy input
model = UpSampleModel()
input_tensor = torch.randn(1, 32, 100)  # Batch size 1, 32 input channels, sequence length 100

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Should be [1, 16, 201] given the parameters
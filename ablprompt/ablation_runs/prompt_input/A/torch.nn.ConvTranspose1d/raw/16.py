import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=1, out_channels=1, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 6)  # Batch size, in channels, sequence length

# Perform the forward pass
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Expected shape: [1, 1, 12]
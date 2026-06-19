import torch
import torch.nn as nn

# Define a simple model using ConvTranspose3d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=8, kernel_size=(3, 3, 3), stride=(2, 2, 2), padding=(1, 1, 1))

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and an input tensor
model = SimpleUpsampler()
input_tensor = torch.randn(1, 1, 4, 8, 16)  # Batch size 1, 1 channel, 4x8x16 spatial dimensions

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape should be [1, 8, 7, 15, 31]
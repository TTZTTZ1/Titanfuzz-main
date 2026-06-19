import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleUpsampler(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels, out_channels, kernel_size, stride, padding)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model
in_channels = 16
out_channels = 8
kernel_size = 4
stride = 2
padding = 1
model = SimpleUpsampler(in_channels, out_channels, kernel_size, stride, padding)

# Generate some random input data
input_data = torch.randn(1, in_channels, 32)

# Perform the forward pass
output_data = model(input_data)

print(output_data.shape)  # Expected shape: torch.Size([1, 8, 65])
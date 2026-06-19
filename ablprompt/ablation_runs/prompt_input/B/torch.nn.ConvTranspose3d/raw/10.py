import torch
from torch import nn

# Define a simple model using ConvTranspose3d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=3, out_channels=64, kernel_size=3, stride=2, padding=1, output_padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and a random input tensor
model = SimpleUpsampler()
input_tensor = torch.randn(1, 3, 8, 16, 32)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape should be [1, 64, 15, 33, 65]
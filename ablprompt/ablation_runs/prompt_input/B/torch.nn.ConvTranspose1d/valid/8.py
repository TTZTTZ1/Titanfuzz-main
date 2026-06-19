import torch
from torch import nn

# Define a simple model using ConvTranspose1d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=3, out_channels=64, kernel_size=5, stride=2, padding=2)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and a random input tensor
model = SimpleUpsampler()
input_tensor = torch.randn(1, 3, 10)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 64, 21])
import torch
from torch import nn

# Define a simple model using ConvTranspose3d
class SimpleUpsampler(nn.Module):
    def __init__(self):
        super(SimpleUpsampler, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=1, out_channels=8, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and run it on some random input
model = SimpleUpsampler()
input_tensor = torch.randn(1, 1, 16, 16, 16)
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected shape: torch.Size([1, 8, 32, 32, 32])
import torch
from torch.nn import ConvTranspose2d

# Define the model
model = ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=3, stride=2, padding=1)

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Perform the forward pass
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Should be [1, 64, 64, 64]
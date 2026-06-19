import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 1, 28, 28)
input_tensor = torch.randn(1, 1, 28, 28)

# Create a random grid tensor of shape (1, 28, 28, 2)
grid_tensor = torch.randn(1, 28, 28, 2)

# Apply grid_sample with bilinear interpolation and zero padding
output_tensor = F.grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)  # Should print torch.Size([1, 1, 28, 28])
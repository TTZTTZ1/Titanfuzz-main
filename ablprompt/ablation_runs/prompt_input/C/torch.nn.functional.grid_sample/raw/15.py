import torch
from torch.nn.functional import grid_sample

# Create a random input tensor
input_tensor = torch.randn(1, 1, 4, 4)

# Create a grid tensor with normalized coordinates
grid_tensor = torch.tensor([[[[0.5, 0.5], [0.5, -0.5]], [[-0.5, 0.5], [-0.5, -0.5]]]])

# Apply grid sample
output_tensor = grid_sample(input_tensor, grid_tensor, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor)
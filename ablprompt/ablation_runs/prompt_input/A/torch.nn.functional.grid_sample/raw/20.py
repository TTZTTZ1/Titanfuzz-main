import torch
import torch.nn.functional as F

# Create a grid of coordinates
grid = torch.tensor([[[[0, 0], [1, 0]], [[0, 1], [1, 1]]]], dtype=torch.float32)

# Create an input tensor
input_tensor = torch.tensor([[[[1., 2.], [3., 4.]]]], dtype=torch.float32)

# Apply grid sample
output_tensor = F.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros')

print(output_tensor)
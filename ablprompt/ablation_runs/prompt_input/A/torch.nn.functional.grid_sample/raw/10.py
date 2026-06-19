import torch
import torch.nn.functional as F

# Create some input tensors
input_tensor = torch.randn(1, 3, 4, 4)
grid = torch.randn(1, 2, 4, 4)

# Call grid_sample
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)
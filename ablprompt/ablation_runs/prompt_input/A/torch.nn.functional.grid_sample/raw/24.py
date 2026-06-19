import torch
import torch.nn.functional as F

# Create input tensor and grid
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size 1, 3 channels, 4x4 spatial dimensions
grid = torch.tensor([[[[0.5, 0.5], [0.5, -0.5]], [[-0.5, 0.5], [-0.5, -0.5]]]])  # Grid for sampling

# Call grid_sample
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)
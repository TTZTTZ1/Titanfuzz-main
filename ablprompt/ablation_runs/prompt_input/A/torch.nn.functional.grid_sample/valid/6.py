import torch
import torch.nn.functional as F

# Create input tensor and grid
input_tensor = torch.randn(1, 1, 4, 4)  # Batch size 1, channels 1, height 4, width 4
grid = torch.tensor([[[[0.5, 0.5], [0.5, -0.5]], [[-0.5, 0.5], [-0.5, -0.5]]]])  # Grid of coordinates

# Apply grid sample
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)
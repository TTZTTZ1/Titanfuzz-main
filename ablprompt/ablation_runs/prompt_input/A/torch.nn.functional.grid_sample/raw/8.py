import torch
import torch.nn.functional as F

# Create input tensor and grid
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size of 1, channels of 3, height of 4, width of 4
grid = torch.tensor([[[[0.5, 0.5], [0.5, 1.5]], [[1.5, 0.5], [1.5, 1.5]]]])  # Grid for sampling

# Call grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)
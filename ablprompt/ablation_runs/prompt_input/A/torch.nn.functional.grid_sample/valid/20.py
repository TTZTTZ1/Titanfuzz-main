import torch
import torch.nn.functional as F

# Create an input tensor and a grid tensor
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size=1, Channels=3, Height=4, Width=4
grid = torch.tensor([[[[0.5, 0.5], [0.5, -0.5]], [[-0.5, 0.5], [-0.5, -0.5]]]])  # Grid coordinates

# Call the grid_sample function
output_tensor = F.grid_sample(input_tensor, grid)

print(output_tensor)
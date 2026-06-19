import torch
from torchvision import transforms

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define a transformation to generate a grid
transform = transforms.Compose([
    transforms.RandomAffine(degrees=30, scale=(0.9, 1.1)),
    transforms.ToTensor()
])

# Apply the transformation to get the grid
grid = transform(input_tensor).unsqueeze(0)

# Ensure the grid is within the [-1, 1] range
grid = grid * 2 - 1

# Perform grid sampling
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)
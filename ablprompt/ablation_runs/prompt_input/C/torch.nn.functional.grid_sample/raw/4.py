import torch
from torchvision import transforms

# Create a random input tensor
input_tensor = torch.randn(1, 1, 64, 64)

# Define an affine transformation matrix
theta = torch.tensor([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], dtype=torch.float32).unsqueeze(0)
grid_generator = transforms.AffineTransformGenerator()
grid = grid_generator(theta, (64, 64))

# Apply grid sampling
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)
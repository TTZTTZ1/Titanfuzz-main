import torch
from torchvision import transforms

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Define an affine transformation matrix
theta = torch.tensor([[1.0, 0.0, 32], [0.0, 1.0, 32]], dtype=torch.float32).unsqueeze(0)
grid = transforms.ToTensor()(transforms.functional.affine(theta, translate=[32, 32]))

# Apply grid_sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros')

print(output_tensor.shape)
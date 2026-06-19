import torch
from torchvision import transforms

# Create a random input tensor
input_tensor = torch.randn(1, 3, 64, 64)

# Create a grid using affine transformation
grid = transforms.functional.affine_grid(torch.tensor([[[0.5, 0, 32], [0, 0.5, 32]]]), input_tensor.size())

# Apply grid sample
output_tensor = torch.nn.functional.grid_sample(input_tensor, grid, mode='bilinear', padding_mode='zeros', align_corners=False)

print(output_tensor.shape)
import torch
from torch.nn import functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Apply interpolation using torch.nn.functional.interpolate
output_tensor = F.interpolate(input_tensor, scale_factor=0.5, mode='bilinear', align_corners=False)

print(output_tensor.shape)
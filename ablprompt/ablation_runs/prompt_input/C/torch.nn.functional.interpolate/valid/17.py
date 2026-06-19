import torch
from torch.nn import functional as F

# Create a random 4D tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Interpolate the tensor to a new size
output_tensor = F.interpolate(input_tensor, size=(64, 64), mode='bilinear', align_corners=True)

print(output_tensor.shape)
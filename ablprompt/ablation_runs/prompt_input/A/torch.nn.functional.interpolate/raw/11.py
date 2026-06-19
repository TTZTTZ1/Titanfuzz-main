import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Interpolate the tensor to a new size
output_tensor = F.interpolate(input_tensor, size=(128, 128), mode='bilinear', align_corners=False)

print(output_tensor.shape)
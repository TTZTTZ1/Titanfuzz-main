import torch
import torch.nn.functional as F

# Create a random input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Use interpolate to resize the input tensor
output_tensor = F.interpolate(input_tensor, size=(128, 128), mode='bilinear', align_corners=False)

print(output_tensor.shape)
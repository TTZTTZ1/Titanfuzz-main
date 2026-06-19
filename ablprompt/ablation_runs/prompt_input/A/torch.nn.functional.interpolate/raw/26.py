import torch
from torch.nn.functional import interpolate

# Example usage of torch.nn.functional.interpolate
input_tensor = torch.randn(1, 3, 256, 256)  # Batch size 1, 3 channels, 256x256 image
output_tensor = interpolate(input_tensor, scale_factor=0.5, mode='bilinear', align_corners=False)
print(output_tensor.shape)  # Expected output shape: [1, 3, 128, 128]
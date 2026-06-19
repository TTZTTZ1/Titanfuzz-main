import torch
import torch.nn.functional as F

# Create a dummy input tensor
input_tensor = torch.randn(1, 3, 256, 256)

# Define interpolation parameters
scale_factor = (0.5, 0.5)
mode = 'bilinear'
align_corners = False

# Call the interpolate function
output_tensor = F.interpolate(input_tensor, scale_factor=scale_factor, mode=mode, align_corners=align_corners)

print(output_tensor.shape)  # Output should be [1, 3, 128, 128]
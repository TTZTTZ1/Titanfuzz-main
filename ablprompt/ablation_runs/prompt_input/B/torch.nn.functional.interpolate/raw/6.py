import torch
from torchvision.transforms import functional as F

# Create a random 4D tensor representing a batch of images
input_tensor = torch.randn(2, 3, 256, 256)

# Define the desired output size
output_size = (128, 128)

# Apply interpolation using bilinear mode
interpolated_tensor = F.interpolate(input_tensor, size=output_size, mode='bilinear', align_corners=True)

print(interpolated_tensor.shape)
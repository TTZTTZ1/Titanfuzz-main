import torch
import torch.nn.functional as F

# Create random input and weight tensors
input_tensor = torch.randn(1, 3, 32, 32)
weight_tensor = torch.randn(64, 3, 3, 3)

# Apply 2D convolution
output_tensor = F.conv2d(input_tensor, weight_tensor, padding=1, stride=2, groups=3)

print(output_tensor.shape)
import torch
import torch.nn.functional as F

# Create a random input tensor and a kernel
input_tensor = torch.randn(1, 3, 32, 32)
kernel = torch.randn(3, 3, 5, 5)

# Apply convolution
output = F.conv2d(input_tensor, kernel, padding=2)

print(output.shape)
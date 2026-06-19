import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 3, 5, 5)
input_tensor = torch.randn(1, 3, 5, 5)

# Create a random convolutional kernel tensor of shape (16, 3, 3, 3)
kernel_tensor = torch.randn(16, 3, 3, 3)

# Perform the convolution operation
output_tensor = F.conv2d(input_tensor, kernel_tensor, stride=1, padding=0)

print(output_tensor.shape)  # Output should be (1, 16, 3, 3)
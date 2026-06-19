import torch
import torch.nn.functional as F

# Create a random input tensor of shape (1, 1, 3, 3)
input_tensor = torch.randn(1, 1, 3, 3)

# Define a convolutional kernel of shape (1, 1, 2, 2)
kernel = torch.tensor([[[[0.5, -0.5], [-0.5, 0.5]]]])

# Perform the 2D convolution
output_tensor = F.conv2d(input_tensor, kernel, padding=1)

print(output_tensor)
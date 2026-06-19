import torch
import torch.nn.functional as F

# Create a random input tensor and a kernel (filter)
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size=1, Channels=3, Height=5, Width=5
kernel = torch.randn(3, 3, 3, 3)       # Out_channels=3, In_channels=3, Kernel_height=3, Kernel_width=3

# Perform convolution
output_tensor = F.conv2d(input_tensor, kernel)

print(output_tensor.shape)  # Output shape should be [1, 3, 3, 3]
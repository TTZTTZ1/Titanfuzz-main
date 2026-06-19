import torch
import torch.nn as nn

# Define input tensor and parameters for Unfold
input_tensor = torch.randn(1, 3, 4, 4)  # Batch size=1, Channels=3, Height=4, Width=4
kernel_size = (2, 2)
stride = (1, 1)
padding = (0, 0)

# Create an instance of Unfold
unfold = nn.Unfold(kernel_size, stride, padding)

# Apply Unfold to the input tensor
output = unfold(input_tensor)

print(output.shape)  # Output shape will be [1, 12, 9] (Batch size * Channels * kernel_size[0] * kernel_size[1], (Height - kernel_size[0] + 2*padding[0]) // stride[0] * (Width - kernel_size[1] + 2*padding[1]) // stride[1])
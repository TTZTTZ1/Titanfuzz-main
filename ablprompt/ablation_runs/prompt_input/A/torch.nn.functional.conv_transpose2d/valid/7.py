import torch
import torch.nn.functional as F

# Create input tensor and weight for the convolutional transpose operation
input_tensor = torch.randn(1, 3, 5, 5)  # Batch size=1, Channels=3, Height=5, Width=5
weight = torch.randn(3, 1, 4, 4)       # Out_channels=3, In_channels=1, Kernel_size=(4, 4)

# Perform the convolutional transpose operation
output_tensor = F.conv_transpose2d(input_tensor, weight, stride=2, padding=1)

print(output_tensor)
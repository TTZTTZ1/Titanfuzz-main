import torch
import torch.nn.functional as F

# Create some random input tensor and weight tensor
input_tensor = torch.randn(1, 3, 5, 5)
weight_tensor = torch.randn(3, 1, 4, 4)

# Call conv_transpose2d
output_tensor = F.conv_transpose2d(input_tensor, weight_tensor, stride=2, padding=1)

print(output_tensor.shape)  # Output shape should be [1, 3, 10, 10]
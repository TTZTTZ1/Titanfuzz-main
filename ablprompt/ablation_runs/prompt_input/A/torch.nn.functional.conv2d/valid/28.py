import torch
import torch.nn.functional as F

# Create a random input tensor and weight tensor
input_tensor = torch.randn(1, 3, 5, 5)
weight_tensor = torch.randn(1, 3, 3, 3)

# Call the conv2d function
output_tensor = F.conv2d(input_tensor, weight_tensor)

print(output_tensor)
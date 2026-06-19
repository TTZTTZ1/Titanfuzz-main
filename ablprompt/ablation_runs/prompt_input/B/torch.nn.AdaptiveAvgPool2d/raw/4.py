import torch
import torch.nn as nn

# Create an AdaptiveAvgPool2d layer with output size (3, 4)
pool = nn.AdaptiveAvgPool2d((3, 4))

# Generate a random input tensor with shape (2, 3, 8, 6)
input_tensor = torch.randn(2, 3, 8, 6)

# Apply the AdaptiveAvgPool2d layer to the input tensor
output_tensor = pool(input_tensor)

print("Input Tensor Shape:", input_tensor.shape)
print("Output Tensor Shape:", output_tensor.shape)
import torch
import torch.nn as nn

# Create an AdaptiveMaxPool2d layer with output size (3, 4)
m = nn.AdaptiveMaxPool2d((3, 4))

# Create a random input tensor with shape (1, 64, 8, 9)
input_tensor = torch.randn(1, 64, 8, 9)

# Apply the AdaptiveMaxPool2d layer to the input tensor
output_tensor = m(input_tensor)

# Print the shapes of the input and output tensors
print("Input shape:", input_tensor.shape)
print("Output shape:", output_tensor.shape)
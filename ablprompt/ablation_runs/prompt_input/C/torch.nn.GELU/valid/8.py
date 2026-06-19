import torch
import torch.nn as nn

# Create a GELU layer with the default 'none' approximation
gelu_layer = nn.GELU()

# Generate a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the GELU activation function
output_tensor = gelu_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
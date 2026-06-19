import torch
import torch.nn as nn

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Apply GELU activation
gelu_layer = nn.GELU(approximate="tanh")
output_tensor = gelu_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
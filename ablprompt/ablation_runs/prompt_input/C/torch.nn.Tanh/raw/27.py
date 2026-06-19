import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply Tanh activation
tanh_layer = nn.Tanh()
output_tensor = tanh_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Tanh:", output_tensor)
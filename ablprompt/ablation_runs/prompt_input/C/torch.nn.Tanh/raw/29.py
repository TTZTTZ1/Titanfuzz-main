import torch
import torch.nn as nn

# Create a Tanh activation layer
tanh_layer = nn.Tanh()

# Define a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Tanh activation
output_tensor = tanh_layer(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after Tanh Activation:")
print(output_tensor)
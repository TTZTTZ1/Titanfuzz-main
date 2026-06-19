import torch
import torch.nn as nn

# Create a Tanh activation layer
tanh = nn.Tanh()

# Generate a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Tanh activation function
output_tensor = tanh(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor:\n", output_tensor)
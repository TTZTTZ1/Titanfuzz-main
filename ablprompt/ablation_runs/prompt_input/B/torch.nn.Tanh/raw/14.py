import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define the Tanh activation function
tanh = nn.Tanh()

# Apply the Tanh function to the input tensor
output_tensor = tanh(input_tensor)

print("Input Tensor:\n", input_tensor)
print("Output Tensor:\n", output_tensor)
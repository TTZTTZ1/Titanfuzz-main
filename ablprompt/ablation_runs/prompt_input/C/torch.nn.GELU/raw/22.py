import torch
import torch.nn as nn

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Define the GELU activation function
gelu = nn.GELU(approximate='tanh')

# Apply the GELU activation function to the input tensor
output_tensor = gelu(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after GELU:")
print(output_tensor)
import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4, requires_grad=True)

# Define the ReLU activation function
relu = nn.ReLU(inplace=False)

# Apply ReLU to the input tensor
output_tensor = relu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 5)

# Define the ReLU activation function
relu = nn.ReLU(inplace=False)

# Apply ReLU to the input tensor
output_tensor = relu(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ReLU:", output_tensor)
import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define the ReLU activation function
relu = nn.ReLU(inplace=True)

# Apply ReLU to the input tensor
output_tensor = relu(input_tensor)

print(output_tensor)
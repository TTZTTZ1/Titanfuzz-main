import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define a ReLU layer
relu_layer = nn.ReLU(inplace=True)

# Apply ReLU to the input tensor
output_tensor = relu_layer(input_tensor)

print(output_tensor)
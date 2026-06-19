import torch
from torch import nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Initialize the Sigmoid layer
sigmoid_layer = nn.Sigmoid()

# Apply the Sigmoid function to the input tensor
output_tensor = sigmoid_layer(input_tensor)

print(output_tensor)
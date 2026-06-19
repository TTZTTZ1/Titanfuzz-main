import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define the Sigmoid layer
sigmoid_layer = nn.Sigmoid()

# Apply the Sigmoid activation function
output_tensor = sigmoid_layer(input_tensor)

print(output_tensor)
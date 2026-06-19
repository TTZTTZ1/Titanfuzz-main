import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Define a Sigmoid layer
sigmoid_layer = nn.Sigmoid()

# Apply the Sigmoid layer to the input tensor
output_tensor = sigmoid_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
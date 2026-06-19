import torch
import torch.nn as nn

# Define a simple linear layer
linear_layer = nn.Linear(in_features=10, out_features=5)

# Create a random input tensor
input_tensor = torch.randn(3, 10)  # Batch size of 3, input features of 10

# Pass the input through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)
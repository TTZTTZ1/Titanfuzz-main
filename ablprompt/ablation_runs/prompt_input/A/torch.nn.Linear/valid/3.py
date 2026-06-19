import torch
import torch.nn as nn

# Create a linear layer with 10 input features and 5 output features
linear_layer = nn.Linear(in_features=10, out_features=5)

# Example input tensor of shape (3, 10)
input_tensor = torch.randn(3, 10)

# Pass the input through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)
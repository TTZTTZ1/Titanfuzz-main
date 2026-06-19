import torch
from torch import nn

# Define a simple linear layer
linear_layer = nn.Linear(in_features=10, out_features=5)

# Create a random input tensor
input_tensor = torch.randn(32, 10)  # batch size of 32, 10 features each

# Pass the input through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)
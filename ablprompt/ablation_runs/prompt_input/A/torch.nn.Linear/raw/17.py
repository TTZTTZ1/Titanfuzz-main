import torch
from torch import nn

# Define a simple linear layer
linear_layer = nn.Linear(in_features=10, out_features=2)

# Example input tensor
input_tensor = torch.randn(5, 10)  # Batch size of 5, 10 features each

# Forward pass through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)
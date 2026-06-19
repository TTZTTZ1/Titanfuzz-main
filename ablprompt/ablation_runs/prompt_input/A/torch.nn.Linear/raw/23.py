import torch
import torch.nn as nn

# Create an instance of Linear layer
linear_layer = nn.Linear(in_features=10, out_features=5)

# Example input tensor
input_tensor = torch.randn(3, 10)  # Batch size of 3, features of 10

# Forward pass through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor)
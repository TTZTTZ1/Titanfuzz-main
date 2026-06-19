import torch
import torch.nn as nn

# Create a linear layer with 10 input features and 20 output features
linear_layer = nn.Linear(10, 20)

# Example input tensor of shape (3, 10)
input_tensor = torch.randn(3, 10)

# Forward pass through the linear layer
output_tensor = linear_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([3, 20])
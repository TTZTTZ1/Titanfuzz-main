import torch
import torch.nn as nn

# Create a Tanh layer
tanh_layer = nn.Tanh()

# Create a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Tanh layer to the input tensor
output_tensor = tanh_layer(input_tensor)

print(output_tensor)
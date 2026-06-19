import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold values
softplus_layer = nn.Softplus(beta=0.5, threshold=10.0)

# Define a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Softplus activation function
output_tensor = softplus_layer(input_tensor)

print(output_tensor)
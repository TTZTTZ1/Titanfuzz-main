import torch
from torch import nn

# Create a Softplus layer with custom beta and threshold
softplus_layer = nn.Softplus(beta=0.5, threshold=10.0)

# Generate some random input data
input_data = torch.randn(3, 4)

# Apply the Softplus activation
output_data = softplus_layer(input_data)

print(output_data)
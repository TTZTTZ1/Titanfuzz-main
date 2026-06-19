import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=15.0)

# Generate random input tensor
input_tensor = torch.randn(3, 4)

# Apply Softplus activation
output_tensor = softplus(input_tensor)

print(output_tensor)
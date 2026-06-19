import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus_layer = nn.Softplus(beta=2.0, threshold=30.0)

# Generate random input tensor
input_tensor = torch.randn(5, 5)

# Apply Softplus activation
output_tensor = softplus_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)
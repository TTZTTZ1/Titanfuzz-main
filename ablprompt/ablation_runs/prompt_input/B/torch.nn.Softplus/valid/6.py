import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=15.0)

# Generate some random input data
input_data = torch.randn(3, 4)

# Apply the Softplus activation function
output_data = softplus(input_data)

print("Input Data:", input_data)
print("Output Data:", output_data)
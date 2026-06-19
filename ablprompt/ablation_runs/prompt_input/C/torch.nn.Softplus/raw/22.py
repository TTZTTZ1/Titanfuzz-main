import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus = nn.Softplus(beta=2.0, threshold=30.0)

# Generate some random input data
input_data = torch.randn(5, 5)

# Apply the Softplus activation
output_data = softplus(input_data)

print("Input Data:\n", input_data)
print("Output Data:\n", output_data)
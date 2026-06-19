import torch

# Create a Softplus layer with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Generate some random input data
input_data = torch.randn(3, 4)

# Apply the Softplus activation
output_data = softplus(input_data)

print(output_data)
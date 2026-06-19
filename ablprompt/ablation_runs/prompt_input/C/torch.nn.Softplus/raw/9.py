import torch

# Create a Softplus layer with custom beta and threshold
softplus_layer = torch.nn.Softplus(beta=2.0, threshold=15.0)

# Generate some random input data
input_data = torch.randn(3, 4)

# Apply the Softplus activation
output_data = softplus_layer(input_data)

print("Input Data:", input_data)
print("Output Data:", output_data)
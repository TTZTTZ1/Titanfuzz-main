import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Initialize the Softplus layer with custom beta and threshold
softplus_layer = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Apply the Softplus activation
output_tensor = softplus_layer(input_tensor)

print(output_tensor)
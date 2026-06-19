import torch
from torch.nn import Softplus

# Create a Softplus instance with custom beta and threshold
softplus = Softplus(beta=0.5, threshold=10.0)

# Generate a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Softplus activation function
output_tensor = softplus(input_tensor)

print(output_tensor)
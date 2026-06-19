import torch
from torch.nn import Softplus

# Create an instance of Softplus with custom beta and threshold
softplus = Softplus(beta=0.5, threshold=10.0)

# Generate some random input data
input_data = torch.randn(3, 4)

# Apply the Softplus activation function
output_data = softplus(input_data)

print(output_data)
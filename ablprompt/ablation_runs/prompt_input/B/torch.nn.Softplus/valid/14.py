import torch
from torch.nn import Softplus

# Create a Softplus instance with custom beta and threshold
softplus = Softplus(beta=0.5, threshold=15.0)

# Generate some random input data
input_data = torch.randn(3, 4, requires_grad=True)

# Apply the Softplus activation function
output = softplus(input_data)

# Compute the gradient of the output with respect to the input
output.backward(torch.ones_like(output))

print("Input:", input_data)
print("Output:", output)
print("Gradient:", input_data.grad)
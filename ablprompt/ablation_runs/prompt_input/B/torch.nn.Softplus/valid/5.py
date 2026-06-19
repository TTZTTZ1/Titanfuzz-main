import torch
import torch.nn as nn

# Create a Softplus layer with custom beta and threshold
softplus = nn.Softplus(beta=0.5, threshold=10.0)

# Generate some random input data
input_data = torch.randn(3, 4, requires_grad=True)

# Apply the Softplus activation
output = softplus(input_data)

# Compute the gradient
loss = output.sum()
loss.backward()

print("Input:", input_data)
print("Output:", output)
print("Gradient:", input_data.grad)
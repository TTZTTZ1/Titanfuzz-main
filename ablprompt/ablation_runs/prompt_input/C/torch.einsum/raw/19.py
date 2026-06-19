import torch

# Create two example tensors
a = torch.randn(2, 3, 4)
b = torch.randn(4, 5)

# Define the Einstein summation equation
equation = 'ijk,kjl->ijl'

# Use torch.einsum to perform the operation
result = torch.einsum(equation, a, b)

print(result)
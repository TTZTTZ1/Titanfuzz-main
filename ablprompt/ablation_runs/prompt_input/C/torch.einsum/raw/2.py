import torch

# Create some example tensors
a = torch.randn(2, 3)
b = torch.randn(3, 4)
c = torch.randn(4, 5)

# Define the einsum equation
equation = 'ijk,jkl->ijl'

# Perform the einsum operation
result = torch.einsum(equation, a, b, c)

print(result)
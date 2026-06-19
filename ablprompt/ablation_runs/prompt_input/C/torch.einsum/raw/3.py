import torch

# Create some sample tensors
a = torch.randn(2, 3, 4)
b = torch.randn(4, 5)

# Define the einsum equation
equation = 'ijk,kj->ij'

# Perform the operation using torch.einsum
result = torch.einsum(equation, a, b)

print(result)
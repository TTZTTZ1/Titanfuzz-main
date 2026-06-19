import torch

# Create some example tensors
a = torch.randn(2, 3, 4)
b = torch.randn(3, 4, 5)

# Define the einsum equation
equation = 'ijk,klm->ijl'

# Perform the operation using torch.einsum
result = torch.einsum(equation, a, b)

print(result)
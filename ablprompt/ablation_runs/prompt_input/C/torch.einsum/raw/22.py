import torch

# Create some example tensors
a = torch.randn(3, 4)
b = torch.randn(4, 5)
c = torch.randn(5, 6)

# Define the einsum equation
equation = 'ijk,klm->ijm'

# Use torch.einsum to perform the operation
result = torch.einsum(equation, a, b, c)

print(result)
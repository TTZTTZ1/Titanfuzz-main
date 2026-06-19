import torch

# Create some example tensors
a = torch.randn(3, 4)
b = torch.randn(4, 5)
c = torch.randn(5, 6)

# Use torch.einsum to compute the tensor product of a, b, and c
result = torch.einsum('ijk,kjl->ijl', a, b, c)

print(result)
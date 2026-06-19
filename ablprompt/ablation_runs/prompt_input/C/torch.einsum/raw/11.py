import torch

# Create some example tensors
a = torch.randn(2, 3)
b = torch.randn(3, 4)
c = torch.randn(4, 5)

# Use torch.einsum to compute a complex operation
result = torch.einsum('ij,jkl->ikl', a, b, c)

print(result)
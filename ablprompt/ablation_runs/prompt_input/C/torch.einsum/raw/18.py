import torch

# Create two random tensors
a = torch.randn(2, 3, 4)
b = torch.randn(4, 5)

# Use torch.einsum to compute the batch matrix product
result = torch.einsum('bij,jkl->bil', a, b)

print(result)
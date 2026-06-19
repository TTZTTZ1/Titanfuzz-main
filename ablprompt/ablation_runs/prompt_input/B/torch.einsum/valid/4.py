import torch

# Create some example tensors
a = torch.randn(2, 3, 4)
b = torch.randn(4, 5)

# Use torch.einsum to perform a batch matrix multiplication
result = torch.einsum('bij,jk->bik', a, b)

print(result)
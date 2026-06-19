import torch

# Create two random tensors
a = torch.randn(2, 3, 4)
b = torch.randn(3, 4)

# Use torch.einsum to compute the batch matrix multiplication
result = torch.einsum('bij,bjk->blk', a, b)

print(result)
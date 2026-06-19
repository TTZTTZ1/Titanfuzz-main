import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the indices of the minimum values along dimension 1, keeping the dimensions
result = torch.argmin(x, dim=1, keepdim=True)
print(result)
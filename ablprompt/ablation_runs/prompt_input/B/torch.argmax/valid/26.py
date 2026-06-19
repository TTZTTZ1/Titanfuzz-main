import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the indices of the maximum values along dimension 1
result = torch.argmax(x, dim=1, keepdim=True)

print(result)
import torch

# Create a random tensor
x = torch.randn(3, 4)

# Find the indices of the minimum values along dimension 1
min_indices = torch.argmin(x, dim=1)

print("Input tensor:")
print(x)
print("Indices of minimum values along dimension 1:")
print(min_indices)
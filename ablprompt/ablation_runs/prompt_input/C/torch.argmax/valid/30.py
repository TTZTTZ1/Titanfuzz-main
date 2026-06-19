import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the indices of the max value along dimension 1
max_indices = torch.argmax(x, dim=1)

print(max_indices)
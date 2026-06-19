import torch

# Create a random tensor
x = torch.randn(3, 4)

# Find the indices of the maximum values along dimension 1
max_indices = torch.argmax(x, dim=1)

print("Input Tensor:")
print(x)
print("Indices of Maximum Values Along Dimension 1:")
print(max_indices)
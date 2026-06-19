import torch

# Create a random tensor
x = torch.randn(3, 4)

# Find the indices of the maximum values along dimension 0
max_indices = torch.argmax(x, dim=0)

print("Original Tensor:")
print(x)
print("Indices of Maximum Values Along Dimension 0:")
print(max_indices)
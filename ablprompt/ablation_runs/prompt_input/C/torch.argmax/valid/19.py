import torch

# Create a random tensor
tensor = torch.randn(3, 4)

# Find the indices of the maximum values along dimension 1
max_indices = torch.argmax(tensor, dim=1)

print("Original Tensor:")
print(tensor)
print("Indices of Maximum Values Along Dimension 1:")
print(max_indices)
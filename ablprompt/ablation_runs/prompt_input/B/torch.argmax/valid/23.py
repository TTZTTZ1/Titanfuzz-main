import torch

# Create a random tensor
tensor = torch.randn(3, 4)

# Find the indices of the maximum values along dimension 0
max_indices = torch.argmax(tensor, dim=0)

print("Input Tensor:")
print(tensor)
print("\nIndices of Maximum Values Along Dimension 0:")
print(max_indices)
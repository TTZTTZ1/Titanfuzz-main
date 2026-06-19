import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the index of the minimum value in the entire tensor
min_index_flat = torch.argmin(x)
print("Index of the minimum value in the flattened tensor:", min_index_flat)

# Find the indices of the minimum values along dimension 1
min_indices_dim1 = torch.argmin(x, dim=1)
print("Indices of the minimum values along dimension 1:", min_indices_dim1)

# Keep the dimensions after finding the minimum values along dimension 1
min_indices_dim1_keepdim = torch.argmin(x, dim=1, keepdim=True)
print("Indices of the minimum values along dimension 1 with keepdim=True:", min_indices_dim1_keepdim)
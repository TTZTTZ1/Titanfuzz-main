import torch

# Create a random tensor
x = torch.randn(3, 4, 5)

# Find the index of the minimum value across the entire tensor
min_index_flat = torch.argmin(x)
print("Index of minimum value in flattened tensor:", min_index_flat)

# Find the indices of the minimum values along dimension 1
min_indices_dim1 = torch.argmin(x, dim=1)
print("Indices of minimum values along dimension 1:", min_indices_dim1)

# Find the indices of the minimum values along dimension 1 and keep the dimensions
min_indices_dim1_keepdim = torch.argmin(x, dim=1, keepdim=True)
print("Indices of minimum values along dimension 1 with keepdim=True:", min_indices_dim1_keepdim)
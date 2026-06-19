import torch

# Create a random tensor
tensor = torch.randn(3, 4)

# Find the index of the minimum value in the entire tensor
min_index_flat = torch.argmin(tensor)
print("Index of the minimum value in the flattened tensor:", min_index_flat)

# Find the indices of the minimum values along dimension 0
min_indices_dim0 = torch.argmin(tensor, dim=0)
print("Indices of the minimum values along dimension 0:", min_indices_dim0)

# Find the indices of the minimum values along dimension 1
min_indices_dim1 = torch.argmin(tensor, dim=1)
print("Indices of the minimum values along dimension 1:", min_indices_dim1)

# Keep dimensions when finding the minimum values along dimension 0
min_indices_dim0_keepdim = torch.argmin(tensor, dim=0, keepdim=True)
print("Indices of the minimum values along dimension 0 with keepdim=True:", min_indices_dim0_keepdim)
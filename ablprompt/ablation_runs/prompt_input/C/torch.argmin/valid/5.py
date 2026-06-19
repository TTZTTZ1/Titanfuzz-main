import torch

# Create a random tensor
tensor = torch.randn(3, 4, 5)

# Find the index of the minimum value in the entire tensor
min_index_flat = torch.argmin(tensor)
print(f"Index of minimum value in the flattened tensor: {min_index_flat}")

# Find the index of the minimum value along dimension 1
min_indices_dim1 = torch.argmin(tensor, dim=1)
print(f"Indices of minimum values along dimension 1: {min_indices_dim1}")

# Find the index of the minimum value along dimension 2, keeping the same number of dimensions
min_indices_dim2_keepdim = torch.argmin(tensor, dim=2, keepdim=True)
print(f"Indices of minimum values along dimension 2 with keepdim=True: {min_indices_dim2_keepdim}")
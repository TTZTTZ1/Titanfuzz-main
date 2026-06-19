import torch

# Create a random tensor with some zero values
tensor = torch.tensor([[0, 1, 0], [2, 0, 3], [0, 0, 0]], dtype=torch.float32)

# Use torch.nonzero to find the indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

print("Indices of non-zero elements:", indices)
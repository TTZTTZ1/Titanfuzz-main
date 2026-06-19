import torch

# Create a sample tensor with some zero and non-zero elements
sample_tensor = torch.tensor([[0, 1, 0], [2, 0, 3]], dtype=torch.int32)

# Use torch.nonzero to find the indices of non-zero elements
indices = torch.nonzero(sample_tensor, as_tuple=True)

print("Indices of non-zero elements:", indices)
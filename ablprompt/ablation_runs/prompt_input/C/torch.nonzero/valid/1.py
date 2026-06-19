import torch

# Create a sample tensor with some zero and non-zero values
sample_tensor = torch.tensor([[0, 1, 0], [2, 0, 3]], dtype=torch.int32)

# Use torch.nonzero to find the indices of non-zero elements
non_zero_indices = torch.nonzero(sample_tensor, as_tuple=True)

print("Non-zero indices:", non_zero_indices)
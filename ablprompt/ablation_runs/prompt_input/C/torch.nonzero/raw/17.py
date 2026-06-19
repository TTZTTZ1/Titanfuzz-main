import torch

# Create a sample tensor with some zero and non-zero values
tensor = torch.tensor([[0, 1, 0], [2, 0, 3]], dtype=torch.int32)

# Use torch.nonzero to find the indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

# Print the result
print(indices)
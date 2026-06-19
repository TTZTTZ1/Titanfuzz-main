import torch

# Create a sample tensor
tensor = torch.tensor([[0, 1, 2], [3, 0, 5]], dtype=torch.int32)

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

# Print the result
print(indices)
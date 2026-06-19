import torch

# Create a random tensor with some zero values
input_tensor = torch.randint(0, 5, (4, 4)).float()

# Use torch.nonzero to find the indices of non-zero elements
non_zero_indices = torch.nonzero(input_tensor, as_tuple=True)

print("Non-zero indices:", non_zero_indices)
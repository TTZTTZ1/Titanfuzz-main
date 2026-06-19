import torch

# Create a random tensor with some zero values
input_tensor = torch.randint(0, 5, (3, 4, 5)).to(torch.float32)

# Use torch.nonzero to find the indices of non-zero elements
non_zero_indices = torch.nonzero(input_tensor, as_tuple=True)

# Print the result
print(non_zero_indices)
import torch

# Create a random tensor with some zero and non-zero values
input_tensor = torch.randint(0, 5, (4, 4)).to(torch.float32)

# Use torch.nonzero to find indices of non-zero elements
non_zero_indices = torch.nonzero(input_tensor > 2, as_tuple=True)

# Print the result
print("Non-zero indices:", non_zero_indices)
import torch

# Create a random tensor with some zero values
tensor = torch.randint(0, 5, (4, 4)).to(torch.float32)

# Use torch.nonzero to find indices of non-zero elements
indices = torch.nonzero(tensor, as_tuple=True)

print("Non-zero indices:", indices)
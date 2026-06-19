import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5])

# Create a mask
mask = torch.tensor([True, False, True, False, True])

# Use torch.masked_select
result = torch.masked_select(tensor, mask)

print(result)
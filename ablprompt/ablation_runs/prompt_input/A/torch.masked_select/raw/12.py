import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5])

# Create a mask
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)

# Use torch.masked_select to select elements where the mask is True
result = torch.masked_select(tensor, mask)

print(result)
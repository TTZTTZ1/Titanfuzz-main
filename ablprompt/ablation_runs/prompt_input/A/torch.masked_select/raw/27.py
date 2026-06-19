import torch

# Create a tensor
tensor = torch.tensor([1, 2, 3, 4, 5])

# Create a mask
mask = torch.tensor([True, False, True, False, True])

# Use torch.masked_select to select elements based on the mask
selected_elements = torch.masked_select(tensor, mask)

print(selected_elements)
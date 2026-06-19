import torch

# Create a sample tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create a boolean mask
mask = torch.tensor([[True, False, True], [False, True, False]])

# Use torch.masked_select to select elements based on the mask
result = torch.masked_select(input_tensor, mask)

print(result)
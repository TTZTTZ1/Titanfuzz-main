import torch

# Create a sample tensor
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Create a mask tensor
mask_tensor = torch.tensor([[True, False], [False, True]])

# Use torch.masked_select to select elements from input_tensor based on mask_tensor
selected_elements = torch.masked_select(input_tensor, mask_tensor)

print(selected_elements)
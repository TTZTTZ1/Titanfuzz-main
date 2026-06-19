import torch

# Create a sample tensor and a mask
input_tensor = torch.tensor([[1, 2], [3, 4]])
mask = torch.tensor([[True, False], [False, True]])

# Use torch.masked_select to select elements based on the mask
selected_elements = torch.masked_select(input_tensor, mask)

print(selected_elements)
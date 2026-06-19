import torch

# Create a sample tensor and a mask
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, False, True], [False, True, False]])

# Use torch.masked_select to get selected elements
selected_elements = torch.masked_select(input_tensor, mask)

print(selected_elements)
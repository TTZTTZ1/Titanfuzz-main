import torch

# Create a sample tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create a mask tensor
mask_tensor = torch.tensor([[True, False, True], [False, True, False]])

# Use torch.masked_select to select elements from the input tensor based on the mask
selected_elements = torch.masked_select(input_tensor, mask_tensor)

print(selected_elements)
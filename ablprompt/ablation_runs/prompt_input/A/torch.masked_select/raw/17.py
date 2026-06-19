import torch

# Create a tensor and a mask
tensor = torch.tensor([1, 2, 3, 4, 5])
mask = tensor > 2

# Use torch.masked_select to select elements from the tensor based on the mask
selected_elements = torch.masked_select(tensor, mask)

print(selected_elements)  # Output: tensor([3, 4, 5])
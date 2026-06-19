import torch

# Create a tensor and a mask
tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])

# Use torch.masked_select to select elements from the tensor based on the mask
result = torch.masked_select(tensor, mask)

print(result)
import torch

# Create a sample input tensor and a mask
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, False, True], [False, True, False]])

# Use torch.masked_select to select elements from input_tensor where the corresponding element in mask is True
result = torch.masked_select(input_tensor, mask)

print(result)
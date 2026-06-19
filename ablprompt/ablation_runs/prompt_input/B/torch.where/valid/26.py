import torch

# Create example tensors
condition = torch.tensor([[True, False], [False, True]])
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])

# Use torch.where for element-wise selection
result = torch.where(condition, x, y)
print(result)
import torch

# Create some example tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Use torch.where to select elements from a or b based on a condition
condition = a > b
result = torch.where(condition, a, b)

print(result)
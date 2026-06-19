import torch

# Create some example tensors
condition = torch.tensor([True, False, True])
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Use torch.where to select elements from x or y based on condition
result = torch.where(condition, x, y)

print(result)
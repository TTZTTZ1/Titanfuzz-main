import torch

# Create some tensors
condition = torch.tensor([True, False, True])
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# Use torch.where to select elements from x or y based on condition
result = torch.where(condition, x, y)

print(result)
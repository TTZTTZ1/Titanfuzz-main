import torch

# Create some tensors
condition = torch.tensor([True, False, True])
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([-1.0, -2.0, -3.0])

# Use torch.where to select elements based on condition
result = torch.where(condition, x, y)

print(result)
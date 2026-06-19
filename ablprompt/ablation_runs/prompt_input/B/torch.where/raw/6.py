import torch

# Create some example tensors
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([5, 6, 7, 8])

# Use torch.where to select elements based on a condition
result = torch.where(x > y, x, y)

print(result)
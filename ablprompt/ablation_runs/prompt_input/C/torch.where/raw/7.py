import torch

# Create some sample tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Use torch.where to select elements based on a condition
result = torch.where(a > b, a, b)

print(result)
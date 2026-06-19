import torch

# Create some example tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Use torch.where to select elements from a or b based on a condition
result = torch.where(a > 2, a, b)

print(result)
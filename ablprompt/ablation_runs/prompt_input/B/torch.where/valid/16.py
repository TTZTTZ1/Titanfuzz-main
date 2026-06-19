import torch

# Create example tensors
a = torch.tensor([[1, 0], [0, 3]])
b = torch.tensor([[4, 5], [6, 7]])

# Use torch.where to select elements based on a condition
result = torch.where(a > 0, a, b)

print(result)
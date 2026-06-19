import torch

# Create sample tensors
a = torch.tensor([[1, 0], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Use torch.where to select elements based on condition
result = torch.where(a > b, a, b)

print(result)
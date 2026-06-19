import torch

# Create some sample tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
c = torch.tensor([[9, 10], [11, 12]])

# Use torch.where to select elements based on a condition
result = torch.where(a > b, a, c)

print(result)
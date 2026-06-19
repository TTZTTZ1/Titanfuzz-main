import torch

# Create some tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Use torch.where to select elements from a or b based on a condition
result = torch.where(a > 2, a, b)

print(result)
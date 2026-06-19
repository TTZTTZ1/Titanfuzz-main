import torch

# Create some example tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])
c = torch.tensor([[9, 10], [11, 12]])

# Use torch.where to select elements from b or c based on condition in a
result = torch.where(a > 2, b, c)

print(result)
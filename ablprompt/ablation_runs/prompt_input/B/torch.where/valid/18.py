import torch

# Create sample tensors
a = torch.tensor([1, 0, 1, 0])
b = torch.tensor([4, 5, 6, 7])

# Use torch.where to select elements from b based on conditions in a
result = torch.where(a == 1, b * 2, b - 2)

print(result)
import torch

# Create two tensors of the same shape
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])

# Use torch.where to conditionally select elements from x and y
condition = x > y
result = torch.where(condition, x, y)

print(result)
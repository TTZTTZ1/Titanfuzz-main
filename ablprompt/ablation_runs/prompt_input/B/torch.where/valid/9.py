import torch

# Create some example tensors
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
condition = x > y

# Use torch.where to select elements based on the condition
result = torch.where(condition, x, y)

print(result)
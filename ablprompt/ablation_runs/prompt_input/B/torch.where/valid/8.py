import torch

# Create sample tensors
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([5, 6, 7, 8])

# Define a condition
condition = x > y

# Use torch.where for element-wise selection
result = torch.where(condition, x, y)

print(result)
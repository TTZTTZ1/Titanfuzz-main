import torch

# Create sample tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Define a condition
condition = a > b

# Use torch.where to select elements based on the condition
result = torch.where(condition, a, b)

print(result)
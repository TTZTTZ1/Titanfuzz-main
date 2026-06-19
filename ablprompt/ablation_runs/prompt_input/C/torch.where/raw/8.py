import torch

# Create some example tensors
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

# Define a condition
condition = a > b

# Use torch.where to select elements based on the condition
result = torch.where(condition, a, b)

print(result)
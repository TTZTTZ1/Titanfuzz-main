import torch

# Create example tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Define a condition
condition = a > b

# Use torch.where for element-wise selection
result = torch.where(condition, a, b)

print(result)
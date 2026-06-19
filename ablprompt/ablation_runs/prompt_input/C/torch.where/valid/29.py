import torch

# Create example tensors
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# Define a condition
condition = x > y

# Use torch.where to select elements based on the condition
result = torch.where(condition, x, y)

print(result)
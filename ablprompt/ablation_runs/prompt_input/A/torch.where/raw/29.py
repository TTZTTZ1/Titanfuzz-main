import torch

# Create some tensors for demonstration
condition = torch.tensor([True, False, True])
x = torch.tensor([10, 20, 30])
y = torch.tensor([40, 50, 60])

# Using torch.where to select elements from x and y based on condition
result = torch.where(condition, x, y)

print(result)
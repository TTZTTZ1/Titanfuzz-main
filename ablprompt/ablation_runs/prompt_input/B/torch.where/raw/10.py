import torch

# Create example tensors
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# Define a condition
condition = x > 2

# Use torch.where for element-wise selection
result = torch.where(condition, x * 2, y * 3)

print(result)
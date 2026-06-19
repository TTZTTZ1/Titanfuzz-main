import torch

# Create some example tensors
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# Define a condition tensor
condition = a > b

# Use torch.where for element-wise selection
result = torch.where(condition, a, b)

print(result)
import torch

# Create some sample tensors
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])
c = torch.tensor([7.0, 8.0, 9.0])

# Define a condition tensor
condition = a > b

# Use torch.where to select elements based on the condition
result = torch.where(condition, a, c)

print(result)
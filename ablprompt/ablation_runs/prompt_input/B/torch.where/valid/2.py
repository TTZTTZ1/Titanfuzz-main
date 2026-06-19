import torch

# Create some example tensors
a = torch.tensor([1, 2, 3, 4])
b = torch.tensor([4, 3, 2, 1])

# Use torch.where for element-wise selection
result = torch.where(a > b, a, b)

print(result)
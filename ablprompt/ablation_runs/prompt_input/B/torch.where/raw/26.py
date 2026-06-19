import torch

# Create some example tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
c = torch.tensor([7, 8, 9])

# Use torch.where for element-wise selection
result = torch.where(a > b, c, a)

print(result)
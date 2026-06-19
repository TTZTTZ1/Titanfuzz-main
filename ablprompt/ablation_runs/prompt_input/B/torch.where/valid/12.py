import torch

# Create some example tensors
x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])
z = torch.tensor([7.0, 8.0, 9.0])

# Use torch.where for element-wise selection
result = torch.where(x > y, x, z)

print(result)
import torch

# Create two tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([2, 3, 4])

# Compute element-wise power using torch.pow
result = torch.pow(a, b)

print(result)
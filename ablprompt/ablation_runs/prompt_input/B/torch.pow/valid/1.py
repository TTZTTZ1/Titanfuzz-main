import torch

# Create two tensors of different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([2])

# Compute element-wise power using broadcasting
result = torch.pow(a, b)

print(result)
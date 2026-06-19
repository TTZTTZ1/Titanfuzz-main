import torch

# Create two tensors of different shapes
a = torch.tensor([1, 2, 3])
b = torch.tensor([[1], [2]])

# Use torch.pow with broadcasting
result = torch.pow(a, b)

print(result)
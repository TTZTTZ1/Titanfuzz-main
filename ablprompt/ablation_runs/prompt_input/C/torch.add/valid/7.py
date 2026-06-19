import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([5])

# Use torch.add to perform element-wise addition with broadcasting
result = torch.add(a, b)

print(result)
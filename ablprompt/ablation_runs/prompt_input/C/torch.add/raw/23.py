import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1])

# Use torch.add to add b to each row of a
result = torch.add(a, b)

print(result)
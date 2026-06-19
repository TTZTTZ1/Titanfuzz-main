import torch

# Create two tensors of different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([2])

# Use torch.pow to raise each element of 'a' to the power of corresponding elements in 'b'
result = torch.pow(a, b)

print(result)
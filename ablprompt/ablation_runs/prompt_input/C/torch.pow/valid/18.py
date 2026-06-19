import torch

# Create two tensors with different shapes
a = torch.tensor([1, 2, 3])
b = torch.tensor([[1], [2], [3]])

# Use torch.pow to raise each element of 'a' to the power of corresponding elements in 'b'
result = torch.pow(a, b)

print(result)
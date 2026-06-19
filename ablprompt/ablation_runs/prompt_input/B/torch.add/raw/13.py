import torch

# Create two tensors with different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1])

# Perform element-wise addition with alpha=2
result = torch.add(a, b, alpha=2)

print(result)
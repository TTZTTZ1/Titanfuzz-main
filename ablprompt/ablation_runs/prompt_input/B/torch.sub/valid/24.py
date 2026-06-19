import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([5, 6])

# Perform element-wise subtraction with alpha=2
result = torch.sub(a, b, alpha=2)

print(result)
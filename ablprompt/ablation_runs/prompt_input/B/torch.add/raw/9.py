import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([5], dtype=torch.float)

# Perform element-wise addition with alpha scaling
result = torch.add(a, b, alpha=2)

print(result)
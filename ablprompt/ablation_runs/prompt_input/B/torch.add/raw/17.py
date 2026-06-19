import torch

# Create two tensors of different shapes but compatible for broadcasting
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
b = torch.tensor([5, 6], dtype=torch.float32)

# Perform element-wise addition with alpha scaling
result = torch.add(a, b, alpha=0.5)

print(result)
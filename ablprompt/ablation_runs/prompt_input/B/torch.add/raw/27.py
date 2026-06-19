import torch

# Create two tensors of different shapes but compatible due to broadcasting
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([1])

# Perform element-wise addition with alpha=2
result = torch.add(a, b, alpha=2)

print(result)
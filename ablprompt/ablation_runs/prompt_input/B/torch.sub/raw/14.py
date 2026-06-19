import torch

# Create two tensors with different shapes
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([5])

# Perform element-wise subtraction with broadcasting and scaling
result = torch.sub(a, b, alpha=-1)

print(result)
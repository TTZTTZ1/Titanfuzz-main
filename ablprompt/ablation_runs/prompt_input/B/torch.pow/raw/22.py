import torch

# Create two tensors
a = torch.tensor([2.0, 3.0, 4.0])
b = torch.tensor([1.5, 2.5, 3.5])

# Compute element-wise exponentiation
result = torch.pow(a, b)

print(result)
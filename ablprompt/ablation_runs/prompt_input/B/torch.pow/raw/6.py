import torch

# Create two tensors
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

# Compute element-wise exponentiation using torch.pow
result = torch.pow(a, b)

print(result)
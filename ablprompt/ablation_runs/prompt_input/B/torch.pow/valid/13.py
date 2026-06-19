import torch

# Create two tensors
base = torch.tensor([1, 2, 3])
exponent = torch.tensor([2, 3, 4])

# Compute element-wise power
result = torch.pow(base, exponent)

print(result)
import torch

# Create two tensors
base = torch.tensor([2, 3])
exponent = torch.tensor([3, 2])

# Call torch.pow
result = torch.pow(base, exponent)

print(result)
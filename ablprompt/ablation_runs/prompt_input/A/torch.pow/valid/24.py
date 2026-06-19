import torch

# Create two tensors
base = torch.tensor([2, 3, 4])
exponent = torch.tensor([3, 2, 1])

# Call the torch.pow function
result = torch.pow(base, exponent)

print(result)
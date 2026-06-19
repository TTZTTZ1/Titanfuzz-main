import torch

# Create two tensors
a = torch.tensor([2.0, 3.0])
b = torch.tensor([3.0, 2.0])

# Call torch.pow
result = torch.pow(a, b)

print(result)
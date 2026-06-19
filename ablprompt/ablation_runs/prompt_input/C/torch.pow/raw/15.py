import torch

# Create two tensors of different shapes
base_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
exponent_tensor = torch.tensor([2])

# Perform element-wise exponentiation using torch.pow
result_tensor = torch.pow(base_tensor, exponent_tensor)

print(result_tensor)
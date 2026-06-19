import torch

# Create two tensors of different shapes
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Perform element-wise exponentiation using torch.pow
result = torch.pow(a.unsqueeze(1), b)

print(result)
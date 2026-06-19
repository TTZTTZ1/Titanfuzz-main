import torch

# Create two tensors
a = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
b = torch.tensor([[7, 8, 9], [10, 11, 12]], dtype=torch.float32)

# Perform element-wise multiplication
result = torch.mul(a, b)

print(result)
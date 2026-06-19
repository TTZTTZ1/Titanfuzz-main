import torch

# Create two random tensors
a = torch.randn(2, 3, 4)
b = torch.randn(4, 5)

# Perform a batch matrix multiplication followed by a sum reduction
result = torch.einsum('bij, jkl -> bik', a, b)

print(result)
import torch

# Create two random tensors
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Call torch.matmul
result = torch.matmul(a, b)

print(result)
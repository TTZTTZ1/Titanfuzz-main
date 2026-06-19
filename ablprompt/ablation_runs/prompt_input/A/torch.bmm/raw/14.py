import torch

# Create two random tensors of shape (2, 3)
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(3, 4)

# Perform batch matrix multiplication
result = torch.bmm(tensor1, tensor2)

print(result)
import torch

# Generate two random tensors as input
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Call the mm API
result = torch.Tensor.mm(a, b)
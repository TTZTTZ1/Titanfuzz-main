import torch

# Create two tensors
t = torch.randn(3, 4, 5)
a = torch.randn(3, 4, 6)
b = torch.randn(3, 6, 5)

# Call the API
result = t.baddbmm_(a, b, beta=1, alpha=1)
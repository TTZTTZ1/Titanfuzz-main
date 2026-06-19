import torch

# Generate input data
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Call the API
result = torch.Tensor.mm(a, b)
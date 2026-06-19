import torch

# Generate valid input data
a = torch.randn(5, 4)
b = torch.randn(4, 3)

# Call the API
result = torch.Tensor.mm(a, b)
import torch

# Prepare valid input data
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Call the API
result = torch.Tensor.mm(a, b)
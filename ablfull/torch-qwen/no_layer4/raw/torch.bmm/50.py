import torch

# Generate input data
a = torch.randn(2, 3, 5)
b = torch.randn(2, 5, 4)

# Call the API
result = torch.bmm(a, b)
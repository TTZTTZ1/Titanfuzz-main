import torch

# Generate input data
a = torch.randn(2, 3, 4)
b = torch.randn(2, 4, 5)

# Call the API
result = torch.bmm(a, b)
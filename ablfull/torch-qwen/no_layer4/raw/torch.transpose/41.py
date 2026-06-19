import torch

# Generate input data
x = torch.randn(2, 3)
dim0, dim1 = 0, 1

# Call the API
result = torch.transpose(x, dim0, dim1)
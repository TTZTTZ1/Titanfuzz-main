import torch

# Generate input data
a = torch.randn(2, 3, 4)
dim0 = 0
dim1 = 2

# Call the API
result = torch.transpose(a, dim0, dim1)
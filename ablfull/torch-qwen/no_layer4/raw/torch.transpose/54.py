import torch

# Prepare valid input data
x = torch.randn(4, 5)
dim0, dim1 = 0, 1

# Call the target API
result = torch.transpose(x, dim0, dim1)
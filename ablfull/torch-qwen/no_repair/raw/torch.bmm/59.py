import torch

# Prepare valid input data
a = torch.randn(5, 3, 4)
b = torch.randn(5, 4, 6)

# Call the API
c = torch.bmm(a, b)
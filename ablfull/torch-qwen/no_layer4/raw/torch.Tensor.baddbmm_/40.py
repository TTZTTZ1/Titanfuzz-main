import torch

# Prepare valid input data
a = torch.randn(4, 5, 6)
b = torch.randn(4, 6, 7)
c = torch.randn(4, 5, 7)

# Call the API
result = c.baddbmm_(a, b, beta=2, alpha=3)
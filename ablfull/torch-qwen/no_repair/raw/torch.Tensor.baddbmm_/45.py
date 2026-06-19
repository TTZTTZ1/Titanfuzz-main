import torch

# Prepare valid input data
a = torch.randn(2, 3, 4)
b1 = torch.randn(2, 3, 5)
b2 = torch.randn(2, 5, 6)

# Call the API
a.baddbmm_(b1, b2, beta=2, alpha=3)
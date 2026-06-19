import torch

# Prepare valid input data
a = torch.randn(3, 4, 5)
b = torch.randn(3, 5, 6)
c = torch.randn(3, 4, 6)

# Call the target API
a.baddbmm_(b, c, beta=0, alpha=1)
import torch

# Prepare valid input data
a = torch.rand((3, 4, 5))
b = torch.rand((3, 5, 6))
c = torch.rand((3, 4, 6))

# Call the API
a.baddbmm_(b, c, beta=0.5, alpha=1.0)
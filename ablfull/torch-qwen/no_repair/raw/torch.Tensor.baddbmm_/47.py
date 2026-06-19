import torch

# Prepare input data
a = torch.randn(2, 3, 4)
b1 = torch.randn(2, 5, 6)
b2 = torch.randn(2, 6, 7)

# Call the API
a.baddbmm_(b1, b2, beta=0.5, alpha=1.5)
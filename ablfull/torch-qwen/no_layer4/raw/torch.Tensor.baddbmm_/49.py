import torch

# Prepare input data
a = torch.randn(5, 3, 4)
batch1 = torch.randn(5, 3, 7)
batch2 = torch.randn(5, 7, 4)

# Call the API
a.baddbmm_(batch1, batch2, beta=0.5, alpha=1.0)
import torch

# Prepare valid input data
self = torch.randn(4, 5, 6)
batch1 = torch.randn(4, 5, 7)
batch2 = torch.randn(4, 7, 8)

# Call the API
self.baddbmm_(batch1, batch2, beta=2, alpha=3)
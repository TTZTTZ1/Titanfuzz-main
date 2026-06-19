import torch

# Prepare valid input data
self = torch.randn(4, 5, 6)
batch1 = torch.randn(4, 5, 6)
batch2 = torch.randn(4, 6, 7)

# Call the API
result = self.baddbmm_(batch1, batch2, beta=2, alpha=3)
import torch

# Prepare valid input data
self = torch.randn(5, 4, 3)
batch1 = torch.randn(5, 4, 3)
batch2 = torch.randn(5, 3, 6)

# Call the API
result = self.baddbmm_(batch1, batch2, beta=1, alpha=1)
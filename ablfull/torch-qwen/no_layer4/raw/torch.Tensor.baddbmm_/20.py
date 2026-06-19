import torch

# Prepare valid input data
self_tensor = torch.randn(3, 4, 5)
batch1 = torch.randn(3, 4, 6)
batch2 = torch.randn(3, 6, 7)

# Call the API
result = self_tensor.baddbmm_(batch1, batch2, beta=1, alpha=1)
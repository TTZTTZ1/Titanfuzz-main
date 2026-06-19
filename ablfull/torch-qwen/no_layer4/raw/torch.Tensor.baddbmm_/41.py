import torch

# Prepare valid input data
batch1 = torch.randn(3, 3, 3)
batch2 = torch.randn(3, 3, 3)
self_tensor = torch.randn(3, 3, 3)

# Call the API
self_tensor.baddbmm_(batch1, batch2, beta=1, alpha=1)
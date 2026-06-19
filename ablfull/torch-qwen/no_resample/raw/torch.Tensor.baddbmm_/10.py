import torch

# Prepare valid input data
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)
beta = 1
alpha = 1
self_tensor = torch.randn(2, 3, 5)

# Call the API
self_tensor.baddbmm_(batch1, batch2, beta=beta, alpha=alpha)
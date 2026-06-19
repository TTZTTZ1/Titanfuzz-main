import torch

# Prepare valid input data
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)

# Call the API
result = batch1.baddbmm_(batch1=beta*batch2, alpha=alpha)
import torch

# Prepare valid input data
batch1 = torch.randn(10, 5)
batch2 = torch.randn(10, 3, 5)
mat = torch.randn(10, 3)

# Call the API
result = batch1.baddbmm_(mat, batch2)
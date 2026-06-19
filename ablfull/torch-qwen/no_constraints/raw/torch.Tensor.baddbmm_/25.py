import torch

# Prepare valid input data
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)
mat = torch.randn(2, 3, 5)

# Call the API
result = batch1.baddbmm_(batch2, mat)
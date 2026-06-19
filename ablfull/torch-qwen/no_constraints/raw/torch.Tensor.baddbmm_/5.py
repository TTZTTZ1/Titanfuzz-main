import torch

# Prepare valid input data
batch1 = torch.randn(2, 3)
mat1 = torch.randn(4, 3)
mat2 = torch.randn(4, 5)

# Call the API
result = batch1.baddbmm_(mat1, mat2)
import torch

# Prepare valid input data
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)

# Call the API
result = torch.Tensor.addmm(mat1, mat2)
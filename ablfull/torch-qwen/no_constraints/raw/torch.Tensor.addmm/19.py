import torch

# Prepare valid input data
batch_size = 2
mat1 = torch.randn(batch_size, 3)
mat2 = torch.randn(batch_size, 4)
mat3 = torch.randn(batch_size, 4)

# Call the API
result = torch.Tensor.addmm(mat1, mat2, mat3)
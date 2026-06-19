import torch

# Prepare input data
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 5)

# Call the API
result = torch.Tensor.addmm(mat1, mat2)
print(result)
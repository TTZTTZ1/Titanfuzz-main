import torch

# Task 2: Prepare valid input data
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 5)

# Task 3: Call the API
result = torch.Tensor.addmm(mat1=mat1, mat2=mat2, beta=1, alpha=1)
print(result)
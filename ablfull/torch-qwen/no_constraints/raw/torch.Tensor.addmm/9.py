import torch

# Task 2: Generate input data
alpha = 0.5
beta = 1.0
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
mat3 = torch.randn(2, 4)

# Task 3: Call the API torch.Tensor.addmm
result = mat1.addmm(beta=beta, alpha=alpha, mat2=mat2, mat3=mat3)
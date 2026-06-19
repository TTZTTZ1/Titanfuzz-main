import torch

# Task 2: Generate input data
alpha = 1.0
beta = 0.5
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
mat3 = torch.randn(2, 4)

# Task 3: Call the API torch.Tensor.addmm
result = torch.Tensor.addmm(mat1, mat2, alpha=alpha, beta=beta, out=mat3)
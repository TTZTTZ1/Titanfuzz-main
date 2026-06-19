import torch
alpha = 0.5
beta = 1.0
mat1 = torch.randn(2, 3)
mat2 = torch.randn(3, 4)
mat3 = torch.randn(2, 4)
result = torch.addmm(mat3, beta=beta, alpha=alpha, mat1=mat1, mat2=mat2)
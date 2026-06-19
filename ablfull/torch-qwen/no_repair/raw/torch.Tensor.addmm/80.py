import torch

# Prepare valid input data
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 2)
beta = 0.5
alpha = 2.0

# Call the API
result = torch.addmm(mat1, mat2, beta=beta, alpha=alpha)

print(result)
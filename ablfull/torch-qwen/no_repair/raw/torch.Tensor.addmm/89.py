import torch

# Prepare valid input data
mat1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
mat2 = torch.tensor([[2.0, 0.0], [1.0, 2.0]])
beta = 1.5
alpha = 2.0

# Call the API
result = torch.addmm(mat1, mat2, beta=beta, alpha=alpha)
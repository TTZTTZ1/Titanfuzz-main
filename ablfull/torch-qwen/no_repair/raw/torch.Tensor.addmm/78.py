import torch

# Prepare valid input data
mat1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
mat2 = torch.tensor([[5.0, 6.0]])
beta = 1
alpha = 1

# Call the API
result = torch.Tensor.addmm(mat1, mat2, beta=beta, alpha=alpha)
print(result)
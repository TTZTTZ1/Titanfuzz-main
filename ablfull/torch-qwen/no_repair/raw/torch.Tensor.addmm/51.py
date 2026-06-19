import torch

# Generate valid input data
mat1 = torch.randn(3, 4)
mat2 = torch.randn(4, 5)
beta = 2
alpha = 3

# Call the API
result = torch.Tensor.addmm(mat1, mat2, beta=beta, alpha=alpha)

print(result)
import torch

# Prepare input data
mat1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
mat2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]], dtype=torch.float)
beta = 1
alpha = 1

# Call the API
result = torch.Tensor.addmm(beta=beta, alpha=alpha, mat1=mat1, mat2=mat2)

print(result)
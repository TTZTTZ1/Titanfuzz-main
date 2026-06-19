import torch

# Task 2: Generate input data
mat1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
mat2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
beta = 1.0
alpha = 1.0

# Task 3: Call the API torch.Tensor.addmm
result = mat1.addmm(beta=beta, alpha=alpha, mat2=mat2)
print(result)
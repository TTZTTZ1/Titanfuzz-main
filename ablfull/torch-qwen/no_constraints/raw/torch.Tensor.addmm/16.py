import torch

# Task 2: Generate input data
alpha = 1.0
beta = 0.5
mat1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
mat2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Task 3: Call the API
result = torch.Tensor.addmm(mat1, mat2, alpha=alpha, beta=beta)
print(result)
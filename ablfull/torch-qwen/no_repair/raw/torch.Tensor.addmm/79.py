import torch

# Generate input data
mat1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.int)
mat2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.int)
beta = 1
alpha = 1

# Call the API
result = torch.Tensor.addmm(mat1, mat2, beta=beta, alpha=alpha)
print(result)
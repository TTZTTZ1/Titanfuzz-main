import torch

# Prepare valid input data
mat1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
mat2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
beta = 1
alpha = 1

# Call the API
result = torch.addmm(beta=beta, alpha=alpha, mat1=mat1, mat2=mat2)

print(result)
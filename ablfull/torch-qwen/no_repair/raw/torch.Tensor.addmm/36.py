import torch

# Generate input data
mat1 = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float)
mat2 = torch.tensor([[5.0, 6.0], [7.0, 8.0]], dtype=torch.float)

# Call the API
result = torch.Tensor.addmm(mat1, mat2)
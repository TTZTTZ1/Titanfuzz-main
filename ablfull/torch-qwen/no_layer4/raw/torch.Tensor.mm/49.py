import torch

# Generate input data
mat1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
mat2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)

# Call the API
result = torch.Tensor.mm(mat1, mat2)
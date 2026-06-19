import torch

# Prepare valid input data
matrix1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
matrix2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)

# Call the API
result = matrix1.mm(matrix2)
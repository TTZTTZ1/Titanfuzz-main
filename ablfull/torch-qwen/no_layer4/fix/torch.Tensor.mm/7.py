import torch
matrix1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
matrix2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)
result = torch.Tensor.mm(matrix1, matrix2)
print(result)
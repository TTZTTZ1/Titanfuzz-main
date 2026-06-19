import torch
batch_size = 2
matrix1 = torch.randn(batch_size, 3, 4)
matrix2 = torch.randn(batch_size, 4, 2)
result = torch.bmm(matrix1, matrix2)
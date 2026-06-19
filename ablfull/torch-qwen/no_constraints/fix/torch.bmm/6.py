import torch
batch_size = 2
mat1 = torch.randn(batch_size, 3, 4)
mat2 = torch.randn(batch_size, 4, 5)
result = torch.bmm(mat1, mat2)
print(result)
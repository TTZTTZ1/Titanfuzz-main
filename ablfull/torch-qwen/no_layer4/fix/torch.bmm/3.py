import torch
input_data = torch.randn(2, 3, 4)
mat2 = torch.randn(2, 4, 5)
result = torch.bmm(input_data, mat2)
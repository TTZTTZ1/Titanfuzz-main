import torch

input = torch.randn(2, 3, 5)
mat2 = torch.randn(2, 5, 4)
out = torch.bmm(input, mat2)
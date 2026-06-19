
import torch
input = torch.randn(2, 5, 3)
mat2 = torch.randn(2, 3, 4)
output = torch.bmm(input, mat2)

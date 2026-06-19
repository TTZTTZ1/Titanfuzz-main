
import torch
input = torch.randn(10, 3, 5)
mat2 = torch.randn(10, 5, 8)
output = torch.bmm(input, mat2)
print(output.shape)


import torch
input_tensor = torch.randn(5, 3, 6)
mat2_tensor = torch.randn(5, 6, 7)
output = torch.bmm(input_tensor, mat2_tensor)

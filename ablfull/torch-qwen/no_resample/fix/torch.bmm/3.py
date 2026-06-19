import torch
input_tensor = torch.randn(5, 3, 4)
mat2_tensor = torch.randn(5, 4, 6)
result = torch.bmm(input_tensor, mat2_tensor)
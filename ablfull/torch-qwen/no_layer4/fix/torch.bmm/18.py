import torch
input_tensor = torch.randn(5, 10, 3)
mat2_tensor = torch.randn(5, 3, 8)
result = torch.bmm(input_tensor, mat2_tensor)
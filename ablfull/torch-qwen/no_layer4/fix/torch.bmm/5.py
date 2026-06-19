import torch
input_tensor = torch.randn(3, 2, 4)
mat2_tensor = torch.randn(3, 4, 5)
result = torch.bmm(input_tensor, mat2_tensor)
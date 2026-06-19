import torch
input_tensor = torch.randn(2, 3, 4)
mat2_tensor = torch.randn(2, 4, 5)
result = torch.bmm(input_tensor, mat2_tensor)
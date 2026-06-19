import torch
input_tensor = torch.randn(10, 5, 3)
mat2_tensor = torch.randn(10, 3, 6)
output_tensor = torch.bmm(input_tensor, mat2_tensor)
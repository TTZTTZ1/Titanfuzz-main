import torch

input_tensor = torch.randn(2, 3, 5)
mat2_tensor = torch.randn(2, 5, 4)

result = torch.bmm(input_tensor, mat2_tensor)
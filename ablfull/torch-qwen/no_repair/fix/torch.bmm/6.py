
import torch
input_tensor = torch.randn(3, 4, 5)
mat2_tensor = torch.randn(3, 5, 6)
result = torch.bmm(input_tensor, mat2_tensor)

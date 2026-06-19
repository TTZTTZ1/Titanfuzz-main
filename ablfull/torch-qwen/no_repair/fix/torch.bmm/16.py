
import torch
input_tensor = torch.randn(3, 5, 8)
mat2_tensor = torch.randn(3, 8, 6)
result = torch.bmm(input_tensor, mat2_tensor)
print(result)

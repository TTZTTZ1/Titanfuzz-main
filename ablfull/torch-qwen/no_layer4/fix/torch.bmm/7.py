import torch
input_tensor = torch.randn(10, 5, 8)
mat2_tensor = torch.randn(10, 8, 3)
result = torch.bmm(input_tensor, mat2_tensor)
print(result)
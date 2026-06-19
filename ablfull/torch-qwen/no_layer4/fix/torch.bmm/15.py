import torch
input_data = torch.randn(10, 5, 8)
mat2_data = torch.randn(10, 8, 3)
result = torch.bmm(input_data, mat2_data)
print(result.shape)
import torch
input_tensor = torch.randn(4, 5)
dim = 0
result = input_tensor.stride(dim)
print(result)
import torch
tensor = torch.randn(4, 5)
dim = 0
result = tensor.stride(dim)
print(result)
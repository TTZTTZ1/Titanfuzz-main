
import torch
tensor = torch.randn(5)
dim = 0
result = tensor.stride(dim)
print(result)

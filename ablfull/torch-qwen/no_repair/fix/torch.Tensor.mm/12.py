
import torch
a = torch.randn(3, 4)
b = torch.randn(4, 2)
result = torch.Tensor.mm(a, b)
print(result)

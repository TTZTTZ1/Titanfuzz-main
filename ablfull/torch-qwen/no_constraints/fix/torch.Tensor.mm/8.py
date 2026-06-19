import torch
a = torch.randn(2, 3)
b = torch.randn(3, 4)
result = torch.Tensor.mm(a, b)
print(result)
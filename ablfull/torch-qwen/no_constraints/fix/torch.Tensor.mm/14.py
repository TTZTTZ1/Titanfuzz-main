import torch
a = torch.randn(2, 3)
b = torch.randn(3, 4)
result = a.mm(b)
print(result)
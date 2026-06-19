import torch

a = torch.randn(3, 3, requires_grad=True)
b = torch.randn(3, 3, requires_grad=True)
c = torch.randn(3, 3, requires_grad=True)

result = torch.mul(a, torch.mul(b, c))
print(result)
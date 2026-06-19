import torch
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0], [6.0]])
result = torch.Tensor.mm(a, b)
print(result)
import torch

a = torch.tensor([[1., 2.]])
b = torch.tensor([[3., 4.], [5., 6.]])
result = torch.Tensor.mm(a, b)
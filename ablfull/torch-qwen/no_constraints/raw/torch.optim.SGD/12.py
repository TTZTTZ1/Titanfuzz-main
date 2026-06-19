import torch

params = [torch.randn(2, requires_grad=True)]
optimizer = torch.optim.SGD(params, lr=0.01)
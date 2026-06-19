import torch

params = [torch.randn(3), torch.randn(4)]
optimizer = torch.optim.SGD(params, lr=0.01)
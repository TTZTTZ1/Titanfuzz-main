import torch

params = [torch.randn(2), torch.randn(3)]
optimizer = torch.optim.SGD(params, lr=0.01)
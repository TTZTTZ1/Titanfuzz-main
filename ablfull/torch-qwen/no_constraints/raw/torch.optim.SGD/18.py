import torch

params = [torch.randn(5), torch.randn(5)]
optimizer = torch.optim.SGD(params, lr=0.01)
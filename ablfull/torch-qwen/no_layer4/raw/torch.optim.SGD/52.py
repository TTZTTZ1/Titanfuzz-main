import torch

params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9
nesterov = True

optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, nesterov=nesterov)
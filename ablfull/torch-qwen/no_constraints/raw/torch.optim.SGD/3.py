import torch

params = [torch.tensor([2.0], requires_grad=True)]
optimizer = torch.optim.SGD(params, lr=0.01)
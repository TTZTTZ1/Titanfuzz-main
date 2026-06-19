import torch

params = [torch.tensor([1.0, 2.0], requires_grad=True), torch.tensor([3.0, 4.0], requires_grad=True)]
optimizer = torch.optim.SGD(params, lr=0.01)
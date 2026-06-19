import torch

model_params = [torch.randn(5, requires_grad=True)]
optimizer = torch.optim.SGD(model_params, lr=0.1, momentum=0)
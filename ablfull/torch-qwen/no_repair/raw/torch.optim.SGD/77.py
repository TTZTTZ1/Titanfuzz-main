import torch

model_params = [torch.randn(3, requires_grad=True)]
optimizer = torch.optim.SGD(model_params, lr=0.01)
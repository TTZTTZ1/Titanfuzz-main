import torch

model_params = [torch.randn(3), torch.randn(4)]
optimizer = torch.optim.SGD(model_params, lr=0.01)
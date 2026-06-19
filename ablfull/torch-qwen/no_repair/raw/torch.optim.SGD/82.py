import torch

model_params = [torch.randn(2, 3), torch.randn(3)]
optimizer = torch.optim.SGD(model_params, lr=0.01)
import torch

# Prepare input data
params = [torch.randn(3), torch.randn(4)]
optimizer = torch.optim.SGD(params, lr=0.001, momentum=0.9, nesterov=False)
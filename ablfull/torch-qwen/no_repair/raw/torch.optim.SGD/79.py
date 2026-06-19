import torch

# Prepare input data
params = [torch.randn(3)]
lr = 0.01
momentum = 0.9 if not nesterov else 0
weight_decay = 0
nesterov = True

# Call the API
optimizer = torch.optim.SGD(params=params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
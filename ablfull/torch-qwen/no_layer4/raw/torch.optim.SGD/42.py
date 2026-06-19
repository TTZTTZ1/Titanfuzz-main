import torch

# Prepare input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9 if not nesterov else 0
weight_decay = 0.0005
nesterov = False

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
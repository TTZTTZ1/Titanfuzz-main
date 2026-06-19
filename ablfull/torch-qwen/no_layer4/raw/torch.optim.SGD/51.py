import torch

# Prepare input data
params = [torch.randn(5, requires_grad=True)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
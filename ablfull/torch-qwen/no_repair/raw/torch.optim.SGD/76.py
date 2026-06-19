import torch
from torch import optim

# Prepare valid input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Create optimizer
optimizer = optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
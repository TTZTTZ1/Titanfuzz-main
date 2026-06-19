import torch

# Prepare valid input data
params = [torch.randn(10), torch.randn(10)]
lr = 0.01
momentum = 0.9
weight_decay = 0.0005
nesterov = False

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
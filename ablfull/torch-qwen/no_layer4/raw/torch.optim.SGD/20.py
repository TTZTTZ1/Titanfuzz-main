import torch

# Prepare input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9
weight_decay = 0.001
nesterov = True

# Ensure the constraint is satisfied
if nesterov:
    momentum = 0.5

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
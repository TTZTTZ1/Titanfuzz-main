import torch

# Generate input data
params = [torch.randn(10), torch.randn(5)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Ensure the constraint is satisfied
if nesterov:
    momentum = 0.1

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
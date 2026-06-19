import torch

# Prepare valid input data
params = [torch.randn(2), torch.randn(2)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Check the constraint before calling the API
if not nesterov or momentum != 0:
    optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
else:
    raise ValueError("Invalid parameters for SGD optimizer")
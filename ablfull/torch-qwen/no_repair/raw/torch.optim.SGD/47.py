import torch

# Prepare valid input data
params = [torch.randn(3)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True
if nesterov:
    assert momentum != 0, "Momentum must be non-zero when nesterov is True"

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
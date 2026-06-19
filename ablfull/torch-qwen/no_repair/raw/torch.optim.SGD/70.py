import torch
from torch.optim import SGD

# Generate input data
params = [torch.tensor([2.0], requires_grad=True)]
lr = 0.1
momentum = 0.9
weight_decay = 1e-4

# Ensure the constraints are met
assert not (nesterov := True) or momentum != 0

# Call the API
optimizer = SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
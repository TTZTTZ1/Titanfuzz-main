import torch

# Prepare valid input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Ensure the constraint is satisfied
if not nesterov or momentum != 0:
    optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
else:
    raise ValueError("Constraint violated: if nesterov is True, momentum must be non-zero")
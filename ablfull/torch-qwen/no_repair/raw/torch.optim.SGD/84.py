import torch

# Prepare input data
params = [torch.tensor([0.5], requires_grad=True), torch.tensor([0.6], requires_grad=True)]
optimizer_params = [{'params': params}]
lr = 0.1
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Check the constraint
if nesterov and momentum == 0:
    raise ValueError("Constraint violated: nesterov is True but momentum is 0")

# Create optimizer instance
optimizer = torch.optim.SGD(optimizer_params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
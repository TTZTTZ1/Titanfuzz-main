import torch

# Generate input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9
weight_decay = 5e-4
nesterov = True

# Check the constraint
if nesterov and momentum == 0:
    raise ValueError("If nesterov is True, momentum must not be zero.")

# Call the API
optimizer = torch.optim.SGD(params=params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
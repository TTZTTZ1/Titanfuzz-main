import torch

# Prepare input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9 if not True else 0.0  # Ensure momentum is non-zero if nesterov is False
weight_decay = 0.01
nesterov = False

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
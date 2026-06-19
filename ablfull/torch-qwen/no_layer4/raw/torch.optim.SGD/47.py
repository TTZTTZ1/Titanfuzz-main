import torch

# Prepare input data
model_params = [torch.tensor([1.0], requires_grad=True)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True

# Check constraint before calling the API
if not nesterov or momentum != 0:
    optimizer = torch.optim.SGD(model_params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
else:
    raise ValueError("Constraint violated: if nesterov is True, momentum must be non-zero.")
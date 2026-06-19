import torch

# Prepare valid input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01
nesterov = True  # This will cause an error because momentum must be non-zero when nesterov is True
fused = None

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov, fused=fused)
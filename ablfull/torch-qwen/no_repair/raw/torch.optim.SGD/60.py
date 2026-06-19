import torch

# Prepare input data
params = [torch.randn(3)]
lr = 0.01
momentum = 0.9
weight_decay = 0.001
nesterov = True
maximize = False
foreach = None
differentiable = False
fused = None

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov, maximize=maximize, foreach=foreach, differentiable=differentiable, fused=fused)
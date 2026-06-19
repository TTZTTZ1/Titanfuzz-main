import torch

# Prepare input data
model_params = [torch.randn(2, requires_grad=True), torch.randn(3, requires_grad=True)]
lr = 0.01
momentum = 0.9
weight_decay = 0.001

# Create optimizer with nesterov set to True and momentum set to 0.9
optimizer = torch.optim.SGD(model_params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=True)
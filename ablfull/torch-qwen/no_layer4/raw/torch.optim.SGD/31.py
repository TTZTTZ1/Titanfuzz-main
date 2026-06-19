import torch

# Generate input data
model_params = [torch.randn(2), torch.randn(3)]
optimizer_params = [{'params': model_params}]
lr = 0.01
momentum = 0.9
weight_decay = 0.001

# Create optimizer instance
optimizer = torch.optim.SGD(optimizer_params, lr=lr, momentum=momentum, weight_decay=weight_decay)
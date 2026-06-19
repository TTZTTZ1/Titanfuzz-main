import torch

# Prepare valid input data
params = [torch.randn(2), torch.randn(3)]
lr = 0.01
momentum = 0.9
weight_decay = 0.0005

# Create an optimizer instance
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
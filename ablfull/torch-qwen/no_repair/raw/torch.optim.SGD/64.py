import torch

# Prepare valid input data
params = [torch.randn(3)]
lr = 0.01
momentum = 0.9
weight_decay = 0.01

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
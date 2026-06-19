import torch
from torch.nn.parameter import Parameter

# Prepare valid input data
model_params = [Parameter(torch.randn(3), requires_grad=True)]
lr = 0.01
momentum = 0.9
weight_decay = 1e-4

# Call the API
optimizer = torch.optim.SGD(model_params, lr=lr, momentum=momentum, weight_decay=weight_decay)
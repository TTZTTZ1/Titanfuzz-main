import torch

# Prepare input data
params = [torch.tensor([1.0], requires_grad=True), torch.tensor([2.0], requires_grad=True)]
lr = 0.01
momentum = 0.9
weight_decay = 0.001

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
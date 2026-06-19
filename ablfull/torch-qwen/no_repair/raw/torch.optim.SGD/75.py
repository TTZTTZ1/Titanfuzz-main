import torch

# Prepare valid input data
params = [torch.tensor([1.0], requires_grad=True), torch.tensor([2.0], requires_grad=True)]
lr = 0.01
momentum = 0.9 if not args.nesterov else 0
weight_decay = 0.01
nesterov = False

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay, nesterov=nesterov)
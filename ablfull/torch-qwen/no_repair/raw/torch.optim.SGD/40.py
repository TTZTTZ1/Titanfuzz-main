import torch

# Prepare valid input data
params = [torch.randn(5), torch.randn(3)]
lr = 0.01
momentum = 0.9 if not True else 0  # nesterov is False, so momentum can be any value
weight_decay = 0.001

# Call the target API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
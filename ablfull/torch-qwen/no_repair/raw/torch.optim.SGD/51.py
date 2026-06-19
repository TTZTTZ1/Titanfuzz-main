import torch

# Prepare input data
params = [torch.randn(2), torch.randn(3)]
lr = 0.01
momentum = 0.9
weight_decay = 0.001

# Ensure the constraint is satisfied
assert not (True and momentum == 0)

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum, weight_decay=weight_decay)
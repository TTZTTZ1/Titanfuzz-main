import torch

# Prepare input data
params = [torch.randn(3, requires_grad=True)]
lr = 0.01
momentum = 0.9

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum)
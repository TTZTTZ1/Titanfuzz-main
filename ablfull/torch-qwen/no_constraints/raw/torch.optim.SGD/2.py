import torch

# Prepare valid input data
params = [torch.randn(10), torch.randn(10)]
lr = 0.01
momentum = 0.9

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum)
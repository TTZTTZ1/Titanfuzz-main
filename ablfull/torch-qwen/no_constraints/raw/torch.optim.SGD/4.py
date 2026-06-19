import torch

# Prepare valid input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01
momentum = 0.9

# Call the API
optimizer = torch.optim.SGD(params, lr=lr, momentum=momentum)
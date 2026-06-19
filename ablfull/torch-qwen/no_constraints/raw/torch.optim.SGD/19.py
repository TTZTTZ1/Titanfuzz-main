import torch

# Prepare valid input data
params = [torch.randn(5), torch.randn(5)]
lr = 0.01

# Call the API
optimizer = torch.optim.SGD(params, lr)
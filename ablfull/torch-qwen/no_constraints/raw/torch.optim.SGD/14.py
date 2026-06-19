import torch

# Prepare input data
params = [torch.randn(3), torch.randn(4)]
lr = 0.01

# Call the API
optimizer = torch.optim.SGD(params, lr)
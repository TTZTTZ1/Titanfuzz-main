import torch

# Prepare valid input data
params = [torch.tensor([2.0, 3.0], requires_grad=True)]
lr = 0.01

# Call the API
optimizer = torch.optim.SGD(params, lr)
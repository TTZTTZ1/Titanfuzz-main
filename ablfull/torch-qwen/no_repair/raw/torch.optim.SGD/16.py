import torch

# Prepare valid input data
model_params = [torch.randn(3, requires_grad=True)]
optimizer = torch.optim.SGD(model_params, lr=0.01, momentum=0.9)
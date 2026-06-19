import torch

# Prepare input data
model_params = [torch.randn(2, requires_grad=True)]
optimizer = torch.optim.SGD(model_params, lr=0.01, momentum=0.9)
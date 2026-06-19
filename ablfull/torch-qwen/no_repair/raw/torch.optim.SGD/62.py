import torch

# Prepare input data
model_params = [torch.randn(4), torch.randn(4)]
optimizer = torch.optim.SGD(model_params, lr=0.01, momentum=0.9, nesterov=False)
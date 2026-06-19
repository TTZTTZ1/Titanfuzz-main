import torch

# Prepare input data
model_params = [torch.randn(2), torch.randn(2)]
optimizer = torch.optim.SGD(model_params, lr=0.01, momentum=0.9)
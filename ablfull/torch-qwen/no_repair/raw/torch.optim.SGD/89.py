import torch

# Prepare input data
model_params = [torch.randn(3), torch.randn(5)]
optimizer = torch.optim.SGD(model_params, lr=0.01)
import torch

# Prepare input data
model_params = [torch.tensor([1.0, 2.0], requires_grad=True)]
optimizer = torch.optim.SGD(model_params, lr=0.01)
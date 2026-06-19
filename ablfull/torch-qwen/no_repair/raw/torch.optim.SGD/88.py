import torch

# Prepare valid input data
model_params = [torch.tensor([0.5], requires_grad=True)]
optimizer_params = {"params": model_params, "lr": 0.1, "momentum": 0.9}
optimizer = torch.optim.SGD(**optimizer_params)
import torch

# Prepare valid input data
model_params = [torch.randn(3, requires_grad=True)]
optimizer_params = {
    'params': model_params,
    'lr': 0.01,
    'momentum': 0.9,
    'weight_decay': 0.01,
    'nesterov': True
}

# Call the API
optimizer = torch.optim.SGD(**optimizer_params)
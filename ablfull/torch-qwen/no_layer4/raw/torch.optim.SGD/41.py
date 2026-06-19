import torch

# Prepare valid input data
model_params = [torch.randn(3, requires_grad=True)]
optimizer_params = model_params
learning_rate = 0.01
momentum = 0.9
weight_decay = 1e-4

# Call the API
optimizer = torch.optim.SGD(optimizer_params, lr=learning_rate, momentum=momentum, weight_decay=weight_decay)
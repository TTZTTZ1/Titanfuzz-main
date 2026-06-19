import torch

# Prepare valid input data
model = torch.nn.Linear(10, 1)
optimizer_params = model.parameters()
learning_rate = 0.01
momentum = 0.9
nesterov = True

# Ensure the constraint is satisfied
if nesterov:
    momentum = 0

# Call the API
optimizer = torch.optim.SGD(optimizer_params, lr=learning_rate, momentum=momentum, nesterov=nesterov)
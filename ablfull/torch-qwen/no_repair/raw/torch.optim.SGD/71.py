import torch

# Prepare input data
model = torch.nn.Linear(10, 5)
optimizer_params = [param for param in model.parameters()]
learning_rate = 0.01
momentum_value = 0.9
nesterov_value = True

# Ensure the constraint is satisfied
if nesterov_value:
    momentum_value = 1.0  # Change momentum to satisfy the constraint

# Call the API
torch.optim.SGD(optimizer_params, lr=learning_rate, momentum=momentum_value, nesterov=nesterov_value)
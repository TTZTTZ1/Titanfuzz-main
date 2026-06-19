import torch

# Prepare valid input data
model_params = [torch.tensor([1.0, -2.0], requires_grad=True), torch.tensor([0.5], requires_grad=True)]
learning_rate = 0.01
momentum_value = 0.9
nesterov_flag = False

# Call the API
optimizer = torch.optim.SGD(model_params, lr=learning_rate, momentum=momentum_value, nesterov=nesterov_flag)
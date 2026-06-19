import torch

# Generate valid input data
model_params = [torch.randn(2), torch.randn(3)]
learning_rate = 0.01
momentum = 0.9
weight_decay = 0.001

# Call the API
optimizer = torch.optim.SGD(model_params, lr=learning_rate, momentum=momentum, weight_decay=weight_decay)
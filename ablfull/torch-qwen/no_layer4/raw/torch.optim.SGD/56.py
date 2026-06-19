import torch

# Prepare input data
model_params = [torch.randn(3), torch.randn(4)]
optimizer_params = model_params

# Call the API
optimizer = torch.optim.SGD(optimizer_params, lr=0.01, momentum=0.9, nesterov=False)
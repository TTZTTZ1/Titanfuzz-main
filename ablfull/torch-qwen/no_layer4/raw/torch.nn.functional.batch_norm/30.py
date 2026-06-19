import torch

# Prepare input data
input_tensor = torch.randn(32, 64, requires_grad=True)
running_mean = torch.zeros(64)
running_var = torch.ones(64)

# Call the API
output = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, training=True)
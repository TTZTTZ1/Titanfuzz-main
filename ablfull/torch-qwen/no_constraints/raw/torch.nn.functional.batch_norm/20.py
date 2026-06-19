import torch

# Prepare valid input data
input_tensor = torch.randn(32, 64, 7, 7)
running_mean = torch.zeros(64)
running_var = torch.ones(64)
weight = torch.ones(64)
bias = torch.zeros(64)

# Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, weight, bias, training=True)
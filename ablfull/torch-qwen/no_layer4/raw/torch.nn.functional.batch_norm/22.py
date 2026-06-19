import torch

# Prepare input data
input_data = torch.randn(10, 3, 32, 32)
running_mean = torch.zeros(3)
running_var = torch.ones(3)

# Call the API
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)
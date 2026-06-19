import torch

# Prepare valid input data
input_data = torch.randn(32, 10)
running_mean = torch.zeros(10)
running_var = torch.ones(10)

# Call the API
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)
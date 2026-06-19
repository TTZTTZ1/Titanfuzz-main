import torch

# Prepare valid input data
input_data = torch.randn(3, 4)
running_mean = torch.zeros(4)
running_var = torch.ones(4)

# Call the API
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)
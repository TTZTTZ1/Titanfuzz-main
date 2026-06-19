import torch

# Prepare valid input data
input_tensor = torch.randn(32, 10)
running_mean = torch.zeros(10)
running_var = torch.ones(10)

# Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var)
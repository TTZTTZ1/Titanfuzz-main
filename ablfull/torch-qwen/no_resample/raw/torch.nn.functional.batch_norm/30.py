import torch

# Prepare input data
input_tensor = torch.randn(32, 16)
running_mean = torch.zeros(16)
running_var = torch.ones(16)

# Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var)
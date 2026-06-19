import torch

# Prepare input data
N, C, H, W = 2, 3, 4, 5
input_tensor = torch.randn(N, C, H, W)
running_mean = torch.zeros(C)
running_var = torch.ones(C)

# Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, training=True)
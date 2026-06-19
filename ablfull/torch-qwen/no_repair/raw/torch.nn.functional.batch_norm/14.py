import torch

# Prepare input data
input_tensor = torch.randn(32, 64, 10, 10, dtype=torch.float32)
running_mean = torch.zeros(64, dtype=torch.float32)
running_var = torch.ones(64, dtype=torch.float32)

# Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, training=True)
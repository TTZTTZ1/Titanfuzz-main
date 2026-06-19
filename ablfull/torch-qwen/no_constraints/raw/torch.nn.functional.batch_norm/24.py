import torch

# Task 2: Generate input data
input_tensor = torch.randn(10, 64, 32, 32)
running_mean = torch.zeros(64)
running_var = torch.ones(64)

# Task 3: Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, training=True)
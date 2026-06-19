import torch

# Task 2: Generate input data
input_tensor = torch.randn(10, 3, 224, 224)
running_mean = torch.zeros(3)
running_var = torch.ones(3)

# Task 3: Call the API
output_tensor = torch.nn.functional.batch_norm(input_tensor, running_mean, running_var, training=True)
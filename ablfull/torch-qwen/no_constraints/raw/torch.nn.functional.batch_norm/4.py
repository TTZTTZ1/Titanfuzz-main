import torch

# Task 2: Generate input data
input_data = torch.randn(10, 3, 224, 224)
running_mean = torch.zeros(3)
running_var = torch.ones(3)

# Task 3: Call the API
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var)
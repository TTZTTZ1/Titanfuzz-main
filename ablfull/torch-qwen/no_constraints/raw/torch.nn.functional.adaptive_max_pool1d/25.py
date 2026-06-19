import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 64, 8)

# Task 3: Call the API
output_tensor = torch.nn.functional.adaptive_max_pool1d(input_tensor, output_size=(4,))
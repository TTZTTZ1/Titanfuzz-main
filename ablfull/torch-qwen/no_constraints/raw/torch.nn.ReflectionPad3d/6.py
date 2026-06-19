import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 2, 2, 2)
padding = (1, 1, 1, 1, 1, 1)

# Task 3: Call the API
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')
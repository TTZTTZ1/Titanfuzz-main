import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 2, 4, 6)

# Task 3: Call the API
padding = (1, 2, 3)
output_tensor = torch.nn.functional.pad(input_tensor, padding, mode='reflect')
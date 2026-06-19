import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3, 4)

# Task 3: Call the API
output_tensor = input_tensor.permute(2, 0, 1)
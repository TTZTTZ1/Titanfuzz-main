import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 5)

# Task 3: Call the API torch.transpose
output_tensor = torch.transpose(input_tensor, 0, 1)
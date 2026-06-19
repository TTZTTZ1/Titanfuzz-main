import torch

# Task 2: Generate input data
input_tensor = torch.randn(2, 3)

# Task 3: Call the API torch.transpose
result = torch.transpose(input_tensor, 0, 1)
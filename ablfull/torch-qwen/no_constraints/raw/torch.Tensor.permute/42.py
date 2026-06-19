import torch

# Task 2: Generate input data
input_tensor = torch.randn(3, 4)

# Task 3: Call the API
permuted_tensor = input_tensor.permute(1, 0)
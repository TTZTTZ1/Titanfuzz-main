import torch

# Task 2: Generate input data
data = torch.randn(2, 3, 4)

# Task 3: Call the API
permuted_data = data.permute(2, 0, 1)
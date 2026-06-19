import torch

# Task 2: Generate input data
tensor = torch.randn(10, 4)

# Task 3: Call the API
split_result = tensor.split([3, 7], dim=0)
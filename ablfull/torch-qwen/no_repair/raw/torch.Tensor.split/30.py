import torch

# Task 2: Generate input data
tensor = torch.randn(10)

# Task 3: Call the API
result = tensor.split(split_size=[4, 3, 3], dim=0)
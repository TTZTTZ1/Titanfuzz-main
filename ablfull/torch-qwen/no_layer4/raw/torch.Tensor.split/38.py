import torch

# Task 2: Generate input data
tensor = torch.randn(4, 5)

# Task 3: Call the API
result = tensor.split(split_size=[2, 2], dim=0)
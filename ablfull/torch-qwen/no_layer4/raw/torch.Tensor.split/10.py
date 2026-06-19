import torch

# Task 2: Generate input data
tensor = torch.randn(10)

# Task 3: Call the API
split_tensors = tensor.split(split_size=[3, 4, 3], dim=0)
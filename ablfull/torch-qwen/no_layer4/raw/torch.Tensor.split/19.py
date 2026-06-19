import torch

# Task 2: Generate input data
tensor = torch.randn(10)

# Task 3: Call the API torch.Tensor.split
split_result = tensor.split(split_size=5, dim=0)
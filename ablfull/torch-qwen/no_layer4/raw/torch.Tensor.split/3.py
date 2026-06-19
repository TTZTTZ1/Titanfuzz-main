import torch

# Task 2: Generate input data
tensor = torch.randn(4, 4)

# Task 3: Call the API torch.Tensor.split
split_result = tensor.split(2, dim=0)
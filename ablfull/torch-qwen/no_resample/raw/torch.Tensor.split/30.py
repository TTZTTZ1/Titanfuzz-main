import torch

# Task 2: Generate input data
tensor = torch.randn(4, 4)

# Task 3: Call the API torch.Tensor.split
result = tensor.split(split_size=[2, 2], dim=0)
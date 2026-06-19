import torch

# Task 2: Generate input data
tensor = torch.randn(2, 3, 4)
dims = (2, 0, 1)

# Task 3: Call the API
result = tensor.permute(dims)
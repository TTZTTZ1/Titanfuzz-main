import torch

# Task 2: Generate input data
tensor = torch.randn(2, 3)
dims = (1, 0)

# Task 3: Call the API
result = tensor.permute(dims)
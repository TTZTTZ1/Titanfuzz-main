import torch

# Task 2: Generate input data
x = torch.randn(2, 3, 4)
dims = (1, 0, 2)

# Task 3: Call the API
result = x.permute(dims)
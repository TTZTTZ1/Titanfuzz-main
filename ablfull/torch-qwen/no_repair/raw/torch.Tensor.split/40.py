import torch

# Task 2: Generate input data
data = torch.randn(10)

# Task 3: Call the API
result = data.split(split_size=[3, 4, 3], dim=0)
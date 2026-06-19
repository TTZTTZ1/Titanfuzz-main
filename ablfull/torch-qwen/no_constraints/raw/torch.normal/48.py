import torch

# Task 2: Generate input data
mean = 0.0
std = 1.0
size = (3, 3)

# Task 3: Call the API
result = torch.normal(mean, std, size)
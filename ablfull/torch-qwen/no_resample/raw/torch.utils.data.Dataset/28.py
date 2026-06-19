import torch

# Task 2: Generate input data
data = [torch.randn(3) for _ in range(10)]

# Task 3: Call the API
dataset = torch.utils.data.Dataset(data)
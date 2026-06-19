import torch

# Task 2: Generate input data
data = [torch.randn(10) for _ in range(5)]

# Task 3: Call the API
dataset = torch.utils.data.Dataset(data)
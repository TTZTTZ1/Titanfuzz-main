import torch

# Task 2: Generate input data
data = torch.randn(2, 3)

# Task 3: Call the API
result = data.permute(1, 0)
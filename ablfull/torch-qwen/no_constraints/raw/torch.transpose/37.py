import torch

# Task 2: Generate input data
x = torch.randn(3, 4)

# Task 3: Call the API torch.transpose
result = torch.transpose(x, 0, 1)
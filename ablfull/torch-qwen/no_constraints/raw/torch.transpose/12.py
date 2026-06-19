import torch

# Task 2: Generate input data
a = torch.randn(4, 5)

# Task 3: Call the API torch.transpose
result = torch.transpose(a, 0, 1)
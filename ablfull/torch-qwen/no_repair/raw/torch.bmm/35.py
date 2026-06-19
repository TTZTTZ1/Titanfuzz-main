import torch

# Task 2: Generate input data
a = torch.randn(2, 3, 4)
b = torch.randn(2, 4, 5)

# Task 3: Call the API
result = torch.bmm(a, b)
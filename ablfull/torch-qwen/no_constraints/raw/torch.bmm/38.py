import torch

# Task 2: Generate input data
a = torch.randn(10, 3, 4)
b = torch.randn(10, 4, 5)

# Task 3: Call the API torch.bmm
result = torch.bmm(a, b)
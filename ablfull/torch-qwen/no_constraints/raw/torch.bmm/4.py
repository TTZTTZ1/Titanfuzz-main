import torch

# Task 2: Generate input data
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Task 3: Call the API torch.bmm
result = torch.bmm(a, b)
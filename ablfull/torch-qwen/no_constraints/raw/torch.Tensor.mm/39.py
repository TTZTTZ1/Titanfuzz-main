import torch

# Task 2: Generate input data
a = torch.randn(5, 3)
b = torch.randn(3, 4)

# Task 3: Call the API
result = torch.Tensor.mm(a, b)
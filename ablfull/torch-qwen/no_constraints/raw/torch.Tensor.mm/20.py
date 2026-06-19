import torch

# Task 2: Generate input data
a = torch.randn(3, 4)
b = torch.randn(4, 5)

# Task 3: Call the API torch.Tensor.mm
result = torch.Tensor.mm(a, b)
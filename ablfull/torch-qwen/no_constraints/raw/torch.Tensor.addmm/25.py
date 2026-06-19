import torch

# Task 2: Generate input data
a = torch.randn(2, 3)
b = torch.randn(3, 4)
c = torch.randn(2, 4)

# Task 3: Call the API torch.Tensor.addmm
result = a.addmm(b, c)
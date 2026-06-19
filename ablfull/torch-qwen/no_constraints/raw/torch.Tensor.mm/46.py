import torch

# Task 2: Generate input data
a = torch.randn(2, 3)
b = torch.randn(3, 4)

# Task 3: Call the API torch.Tensor.mm
result = a.mm(b)
print(result)
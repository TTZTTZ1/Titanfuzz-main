import torch

# Task 2: Generate input data
tensor = torch.randn(3, 4)
dims = (1, 0)

# Task 3: Call the API
result = tensor.permute(dims)
print(result)
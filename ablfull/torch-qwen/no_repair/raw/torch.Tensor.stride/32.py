import torch

# Task 2: Generate input data
tensor = torch.randn(4, 4)

# Task 3: Call the API
result = tensor.stride()

print(result)
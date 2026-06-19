import torch

# Task 2: Generate input data
data = torch.randn(4, 5)

# Task 3: Call the API
result = data.stride()
print(result)
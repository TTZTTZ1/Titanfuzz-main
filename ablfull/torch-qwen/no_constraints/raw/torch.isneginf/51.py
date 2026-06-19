import torch

# Task 2: Generate input data
x = torch.tensor(-float('inf'))

# Task 3: Call the API
result = torch.isneginf(x)
print(result)
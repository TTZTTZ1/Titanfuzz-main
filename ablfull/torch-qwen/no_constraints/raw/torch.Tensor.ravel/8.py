import torch

# Task 2: Generate input data
data = torch.tensor([[1, 2], [3, 4]])

# Task 3: Call the API
result = data.ravel()

print(result)
import torch

# Task 2: Generate input data
a = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Task 3: Call the API
result = torch.linalg.inv(a)
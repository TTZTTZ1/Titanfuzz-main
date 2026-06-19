import torch

# Task 2: Generate input data
a = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float64)

# Task 3: Call the API
result = torch.linalg.inv(a)
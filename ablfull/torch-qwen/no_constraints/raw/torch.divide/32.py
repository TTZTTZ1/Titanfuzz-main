import torch

# Task 2: Generate input data
a = torch.tensor([4.0, 8.0], dtype=torch.float32)
b = torch.tensor([2.0, 4.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.divide(a, b)
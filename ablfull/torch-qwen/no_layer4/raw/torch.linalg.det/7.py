import torch

# Task 2: Generate input data
A = torch.randn(3, 3)

# Task 3: Call the API torch.linalg.det
result = torch.linalg.det(A)
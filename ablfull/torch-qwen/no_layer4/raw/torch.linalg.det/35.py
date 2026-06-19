import torch

# Task 2: Generate input data
A = torch.randn(4, 4, dtype=torch.float64)

# Task 3: Call the API
result = torch.linalg.det(A)
print(result)
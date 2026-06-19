import torch

# Task 2: Generate input data
A = torch.tensor([[4., 7.], [2., 6.]], dtype=torch.float)

# Task 3: Call the API
result = torch.linalg.det(A)
print(result)
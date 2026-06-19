import torch

# Task 2: Generate input data
A = torch.tensor([[4.0, 7.0], [2.0, 6.0]], dtype=torch.float)

# Task 3: Call the API torch.linalg.det
result = torch.linalg.det(A)
print(result)
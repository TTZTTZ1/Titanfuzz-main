import torch

# Task 2: Generate input data
A = torch.tensor([[4.0, -2.0], [1.0, 1.0]])

# Task 3: Call the API
result = torch.slogdet(A)

print(result)
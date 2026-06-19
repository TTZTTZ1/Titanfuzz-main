import torch

# Task 2: Generate valid input data
a = torch.tensor([[4., 7.], [2., 6.]])

# Task 3: Call the API torch.linalg.inv
result = torch.linalg.inv(a)

print(result)
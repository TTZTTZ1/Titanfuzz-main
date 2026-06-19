import torch

# Task 2: Generate input data
a = torch.tensor([[1, 0, 0], [0, 1, 0]])
b = torch.tensor([[0, 0, 1], [1, 0, 0]])

# Task 3: Call the API
result = a.cross(b)
print(result)
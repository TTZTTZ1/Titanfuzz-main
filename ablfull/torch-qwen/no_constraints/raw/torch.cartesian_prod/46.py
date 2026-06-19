import torch

# Task 2: Generate input data
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([5, 6])

# Task 3: Call the API
result = torch.cartesian_prod(a, b)
print(result)
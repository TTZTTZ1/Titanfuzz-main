import torch

# Task 2: Generate input data
a = torch.tensor([1, 2])
b = torch.tensor([3, 4])

# Task 3: Call the API
result = torch.cartesian_prod(a, b)
print(result)
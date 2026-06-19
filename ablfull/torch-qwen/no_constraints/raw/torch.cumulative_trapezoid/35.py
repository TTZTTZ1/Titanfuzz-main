import torch

# Task 2: Generate input data
y = torch.tensor([0., 1., 4., 9., 16.])
x = torch.tensor([0., 1., 2., 3., 4.])

# Task 3: Call the API
result = torch.cumulative_trapezoid(y, x)
print(result)
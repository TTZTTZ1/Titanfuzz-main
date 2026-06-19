import torch

# Task 2: Generate input data
x = torch.tensor([0.0, 1.0, 2.0, 3.0])
y = torch.tensor([1.0, 4.0, 9.0, 16.0])

# Task 3: Call the API
result = torch.cumulative_trapezoid(y, x)

print(result)
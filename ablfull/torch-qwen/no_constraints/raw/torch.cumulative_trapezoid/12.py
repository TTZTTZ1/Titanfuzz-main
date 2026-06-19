import torch

# Task 2: Generate input data
x = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float64)
y = torch.tensor([0.0, 1.0, 4.0, 9.0], dtype=torch.float64)

# Task 3: Call the API
result = torch.cumulative_trapezoid(y, x, dx=None, axis=-1, initial=None)

print(result)
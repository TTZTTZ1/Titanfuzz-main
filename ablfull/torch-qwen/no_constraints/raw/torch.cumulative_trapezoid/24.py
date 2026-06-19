import torch

# Task 2: Generate input data
x = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float32)
y = torch.tensor([0.0, 1.0, 4.0, 9.0], dtype=torch.float32)

# Task 3: Call the API
result = torch.cumulative_trapezoid(y, x, dx=1.0)
print(result)
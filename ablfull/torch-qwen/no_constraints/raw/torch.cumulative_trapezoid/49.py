import torch

# Task 2: Generate input data
x = torch.tensor([0, 1, 2, 3])
y = torch.tensor([4, 5, 6, 7])

# Task 3: Call the API
result = torch.cumulative_trapezoid(y, x)
print(result)
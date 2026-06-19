import torch

# Task 2: Generate input data
r = torch.tensor([1.0])
theta = torch.tensor([0.0])

# Task 3: Call the API torch.polar
result = torch.polar(r, theta)
print(result)
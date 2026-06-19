import torch

# Task 2: Generate input data
r = torch.tensor([1.0, 2.0])
theta = torch.tensor([0.5 * torch.pi, 1.0 * torch.pi])

# Task 3: Call the API torch.polar
result = torch.polar(r, theta)
print(result)
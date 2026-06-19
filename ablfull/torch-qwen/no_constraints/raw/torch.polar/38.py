import torch

# Task 2: Generate input data
r = torch.tensor([1.0], dtype=torch.float32)
theta = torch.tensor([0.5], dtype=torch.float32)

# Task 3: Call the API
result = torch.polar(r, theta)
print(result)
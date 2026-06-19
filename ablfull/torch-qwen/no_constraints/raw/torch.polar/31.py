import torch

# Task 2: Generate valid input data
r = torch.tensor([1.0, 2.0], dtype=torch.float32)
theta = torch.tensor([0.0, 90.0] * 360 // 180, dtype=torch.float32)  # Convert degrees to radians

# Task 3: Call the API
result = torch.polar(r, theta)

print(result)
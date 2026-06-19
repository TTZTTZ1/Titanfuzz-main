import torch

# Task 2: Generate input data
a = torch.tensor([1.0, 2.0])
b = torch.tensor([4.0, 5.0])
weight = 0.5

# Task 3: Call the API
a.lerp_(b, weight)
print(a)
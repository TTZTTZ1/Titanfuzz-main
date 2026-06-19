import torch

# Task 2: Generate input data
mean = torch.tensor([0.0])
stddev = torch.tensor([1.0])

# Task 3: Call the API
result = torch.normal(mean, stddev)

print(result)
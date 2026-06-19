import torch

# Task 2: Generate input data
mean = torch.tensor([0.0])
std_dev = torch.tensor([1.0])

# Task 3: Call the API torch.normal
result = torch.normal(mean, std_dev)
print(result)
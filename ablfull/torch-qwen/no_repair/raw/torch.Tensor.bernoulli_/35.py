import torch

# Task 2: Generate input data
p = 0.7

# Task 3: Call the API
result = torch.tensor([1.0, 0.0]).bernoulli_(p)

print(result)
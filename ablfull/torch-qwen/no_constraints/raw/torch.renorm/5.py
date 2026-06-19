import torch

# Task 2: Generate input data
tensor = torch.randn(3, 4)
p_norm = 2
dim = 0
max_norm = 1.0

# Task 3: Call the API
result = torch.renorm(tensor, p_norm, dim, max_norm)

print(result)
import torch

# Task 2: Generate input data
x = torch.tensor([2.0], dtype=torch.float32)

# Task 3: Call the API torch.arccosh
result = torch.arccosh(x)
print(result)
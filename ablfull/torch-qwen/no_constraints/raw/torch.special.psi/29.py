import torch

# Task 2: Generate input data
x = torch.tensor([1.0])

# Task 3: Call the API
result = torch.special.psi(x)
print(result)
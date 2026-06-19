import torch

# Task 2: Generate input data
x = torch.tensor([False, False, True])

# Task 3: Call the API torch.any
result = torch.any(x)

print(result)
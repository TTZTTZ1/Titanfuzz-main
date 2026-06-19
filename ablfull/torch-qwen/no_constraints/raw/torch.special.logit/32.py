import torch

# Task 2: Generate input data
x = torch.tensor([0.5, 0.7])

# Task 3: Call the API
result = torch.special.logit(x)
print(result)
import torch

# Task 2: Generate input data
x = torch.tensor([0.5], dtype=torch.float32)

# Task 3: Call the API
result = torch.special.logit(x)
print(result)
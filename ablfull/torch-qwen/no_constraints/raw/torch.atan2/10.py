import torch

# Task 2: Generate input data
x = torch.tensor([0.5])
y = torch.tensor([0.5])

# Task 3: Call the API torch.atan2
result = torch.atan2(y, x)
print(result)
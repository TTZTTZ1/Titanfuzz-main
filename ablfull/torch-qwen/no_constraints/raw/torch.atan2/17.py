import torch

# Task 2: Generate input data
x = torch.tensor(1.0)
y = torch.tensor(0.0)

# Task 3: Call the API
result = torch.atan2(y, x)
print(result)
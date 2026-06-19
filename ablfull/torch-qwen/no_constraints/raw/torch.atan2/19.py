import torch

# Task 2: Generate input data
y = torch.tensor(1.0)
x = torch.tensor(1.0)

# Task 3: Call the API
result = torch.atan2(y, x)
print(result)
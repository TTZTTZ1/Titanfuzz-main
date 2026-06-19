import torch

# Task 2: Generate input data
x = torch.tensor([1.0], dtype=torch.float32)
y = torch.tensor([0.0], dtype=torch.float32)

# Task 3: Call the API torch.atan2
result = torch.atan2(y, x)
print(result)
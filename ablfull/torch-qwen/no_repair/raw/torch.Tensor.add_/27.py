import torch

# Task 2: Generate input data
x = torch.tensor([1.0, 2.0], dtype=torch.float)
y = torch.tensor([3.0, 4.0], dtype=torch.float)

# Task 3: Call the API
result = x.add_(y)
print(result)
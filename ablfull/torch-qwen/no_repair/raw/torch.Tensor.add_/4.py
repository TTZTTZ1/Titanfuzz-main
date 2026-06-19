import torch

# Task 2: Generate input data
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
y = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float)

# Task 3: Call the API
x.add_(y, alpha=2)
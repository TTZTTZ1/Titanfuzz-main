import torch

# Task 2: Prepare valid input data
x = torch.randn(3, 4)
y = torch.randn(4, 5)

# Task 3: Call the API
result = torch.bmm(x, y)
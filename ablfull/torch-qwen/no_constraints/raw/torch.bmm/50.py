import torch

# Task 2: Generate input data
batch1 = torch.randn(10, 3, 5)
batch2 = torch.randn(10, 5, 4)

# Task 3: Call the API
result = torch.bmm(batch1, batch2)
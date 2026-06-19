import torch

# Task 2: Generate input data
batch1 = torch.randn(2, 3, 4)
batch2 = torch.randn(2, 4, 5)
mat = torch.randn(2, 3, 5)

# Task 3: Call the API
result = batch1.baddbmm_(mat, batch2)
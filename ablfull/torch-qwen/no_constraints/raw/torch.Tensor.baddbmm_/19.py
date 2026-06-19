import torch

# Task 2: Generate input data
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
batch3 = torch.randn(10, 3, 5)

# Task 3: Call the API
result = batch1.baddbmm_(batch2, batch3)
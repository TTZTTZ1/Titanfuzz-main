import torch

# Task 2: Generate input data
batch1 = torch.randn(2, 3)
batch2 = torch.randn(2, 4, 3)
mat = torch.randn(2, 4)

# Task 3: Call the API
result = batch1.baddbmm_(batch2, mat)
print(result)
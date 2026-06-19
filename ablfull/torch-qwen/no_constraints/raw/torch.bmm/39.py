import torch

# Task 2: Generate input data
batch_size = 2
matrices1 = torch.randn(batch_size, 3, 4)
matrices2 = torch.randn(batch_size, 4, 5)

# Task 3: Call the API torch.bmm
result = torch.bmm(matrices1, matrices2)
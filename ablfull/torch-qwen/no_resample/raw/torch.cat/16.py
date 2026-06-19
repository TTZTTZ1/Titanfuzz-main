import torch

# Task 2: Generate input data
tensors = [torch.randn(3), torch.randn(3)]
dim = 0

# Task 3: Call the API torch.cat
result = torch.cat(tensors, dim)
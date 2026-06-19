import torch

# Task 2: Generate input data
tensors = [torch.tensor([1, 2, 3]), torch.tensor([4, 5])]
dim = 0

# Task 3: Call the API torch.cat
result = torch.cat(tensors, dim)
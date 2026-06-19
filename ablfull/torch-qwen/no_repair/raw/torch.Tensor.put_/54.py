import torch

# Task 2: Generate input data
index = torch.tensor([0, 1, 2])
source = torch.tensor([3, 4, 5])

# Task 3: Call the API
result = torch.Tensor().put_(index, source)
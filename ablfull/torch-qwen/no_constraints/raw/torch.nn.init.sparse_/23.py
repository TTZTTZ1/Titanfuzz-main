import torch

# Task 2: Generate input data
tensor = torch.zeros(4, 4)
sparsity = 0.5

# Task 3: Call the API
result = torch.nn.init.sparse_(tensor, sparsity)
import torch

# Task 2: Generate input data
tensor = torch.zeros(3, 4)
sparsity = 0.5
std = 0.02
generator = torch.Generator().manual_seed(0)

# Task 3: Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std, generator)
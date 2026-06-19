import torch

# Task 2: Generate input data
tensor = torch.zeros(4, 5)
sparsity = 0.8
std = 0.01

# Task 3: Call the API
result_tensor = torch.nn.init.sparse_(tensor, sparsity, std)
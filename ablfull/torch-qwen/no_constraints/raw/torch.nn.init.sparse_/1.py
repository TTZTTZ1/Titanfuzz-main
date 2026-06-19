import torch

# Task 2: Generate input data
tensor = torch.zeros(5, 5)
sparsity = 0.75
std = 0.01

# Task 3: Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std)

print(result)
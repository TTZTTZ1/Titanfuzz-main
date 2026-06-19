import torch

# Task 2: Generate input data
tensor = torch.zeros(3, 4)
sparsity = 0.5
std = 0.01

# Task 3: Call the API
result = torch.nn.init.sparse_(tensor, sparsity, std)

print(result)
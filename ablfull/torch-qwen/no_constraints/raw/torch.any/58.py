import torch

# Task 2: Generate input data - create a tensor with at least one non-zero element
x = torch.tensor([[0, 0], [0, 1]])

# Task 3: Call the API torch.any
result = torch.any(x)
print(result)
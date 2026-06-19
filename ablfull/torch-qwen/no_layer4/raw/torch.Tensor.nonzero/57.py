import torch

# Task 2: Generate input data
tensor = torch.tensor([[0, 1], [2, 0]])

# Task 3: Call the API
result = tensor.nonzero(as_tuple=True)
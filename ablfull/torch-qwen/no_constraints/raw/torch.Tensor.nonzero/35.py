import torch

# Task 2: Generate input data
tensor = torch.tensor([[1, 0], [0, 2]])

# Task 3: Call the API torch.Tensor.nonzero
result = tensor.nonzero()
print(result)
import torch

# Task 2: Generate input data
tensor = torch.tensor([1.0])
other = torch.tensor([2.0])

# Task 3: Call the API
result = tensor.add_(other)
print(result)
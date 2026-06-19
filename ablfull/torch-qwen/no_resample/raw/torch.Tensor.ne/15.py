import torch

# Task 2: Generate input data
tensor = torch.tensor([1.0, 2.0, 3.0])
other = 2.5

# Task 3: Call the API
result = tensor.ne(other)
print(result)
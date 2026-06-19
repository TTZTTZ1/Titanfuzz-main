import torch

# Task 2: Generate input data
tensor = torch.tensor([1, 2, 3], dtype=torch.float)
other = torch.tensor([1, 0, 3], dtype=torch.float)

# Task 3: Call the API
result = tensor.ne(other)
print(result)
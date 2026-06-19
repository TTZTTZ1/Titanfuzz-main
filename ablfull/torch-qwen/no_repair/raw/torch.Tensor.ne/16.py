import torch

# Task 2: Generate input data
a = torch.tensor([1, 2, 3], dtype=torch.int)
b = torch.tensor([1, 0, 3], dtype=torch.int)

# Task 3: Call the API
result = a.ne(b)
print(result)
import torch

# Task 2: Generate input data
a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 2, 6])

# Task 3: Call the API
result = a.ne(b)

print(result)
import torch

# Task 2: Generate input data
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([1.0, 2.5, 3.0])

# Task 3: Call the API
result = a.ne(b)
print(result)
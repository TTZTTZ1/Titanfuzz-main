import torch

# Task 2: Generate input data
x = torch.tensor([1.0, 2.0, 3.0])
y = 2.5

# Task 3: Call the API
result = x.ne(y)
print(result)
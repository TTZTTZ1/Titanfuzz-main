import torch

# Task 2: Generate input data
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
y = torch.tensor([1.0, 2.5, 3.0])

# Task 3: Call the API torch.Tensor.ne
result = x.ne(y)

print(result)
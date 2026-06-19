import torch

# Task 2: Generate input data
a = torch.tensor([1, 2, 3])
b = torch.tensor([1, 0, 3])

# Task 3: Call the API torch.Tensor.ne
result = a.ne(b)
print(result)
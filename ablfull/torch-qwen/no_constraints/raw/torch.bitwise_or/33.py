import torch

# Task 2: Generate input data
a = torch.tensor([1, 0, 3], dtype=torch.int64)
b = torch.tensor([4, 5, 6], dtype=torch.int64)

# Task 3: Call the API torch.bitwise_or
result = torch.bitwise_or(a, b)
print(result)
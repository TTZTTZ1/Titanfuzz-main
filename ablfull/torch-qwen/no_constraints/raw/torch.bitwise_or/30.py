import torch

# Task 2: Generate input data
a = torch.tensor([1, 0, 3], dtype=torch.int32)
b = torch.tensor([4, 5, 6], dtype=torch.int32)

# Task 3: Call the API
result = torch.bitwise_or(a, b)
print(result)
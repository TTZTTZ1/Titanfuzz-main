import torch

# Task 2: Generate input data
a = torch.tensor([1, 0, 1, 1], dtype=torch.uint8)
b = torch.tensor([0, 1, 1, 0], dtype=torch.uint8)

# Task 3: Call the API
result = torch.bitwise_or(a, b)
print(result)
import torch

# Task 2: Generate input data
a = torch.tensor([1, 0, 0], dtype=torch.float32)
b = torch.tensor([0, 1, 0], dtype=torch.float32)

# Task 3: Call the API
result = torch.Tensor.cross(a, b)
print(result)
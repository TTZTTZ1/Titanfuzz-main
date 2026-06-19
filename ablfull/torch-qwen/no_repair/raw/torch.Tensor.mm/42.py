import torch

# Task 2: Generate input data
a = torch.tensor([[1, 2], [3, 4]], dtype=torch.float)
b = torch.tensor([[5, 6], [7, 8]], dtype=torch.float)

# Task 3: Call the API
result = torch.Tensor.mm(a, b)
print(result)
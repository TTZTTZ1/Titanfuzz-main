import torch

# Task 2: Generate input data
a = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
b = torch.tensor([[0, 1, 0], [0, 0, 1], [1, 0, 0]])

# Task 3: Call the API torch.Tensor.cross
result = a.cross(b)
print(result)
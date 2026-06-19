import torch

# Task 2: Generate input data
a = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = torch.tensor([[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]])

# Task 3: Call the API torch.Tensor.cross
result = a.cross(b)
print(result)
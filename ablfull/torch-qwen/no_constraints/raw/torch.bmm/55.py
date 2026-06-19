import torch

# Task 2: Generate input data
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

# Task 3: Call the API torch.bmm
result = torch.bmm(a, b)
print(result)
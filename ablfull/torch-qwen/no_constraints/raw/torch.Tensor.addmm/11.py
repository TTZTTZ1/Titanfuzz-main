import torch

# Task 2: Generate input data
a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
beta = 2.0
alpha = 3.0

# Task 3: Call the API
result = torch.Tensor.addmm(beta * b, alpha * a)
print(result)
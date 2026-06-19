import torch

# Task 2: Generate input data
a = torch.tensor(0.5)
b = torch.tensor(1.0)

# Task 3: Call the API
result = torch.Tensor.nextafter_(a, b)
print(result)
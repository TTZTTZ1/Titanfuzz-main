import torch

# Task 2: Generate valid input data
a = torch.tensor([4., 5., 6.])
b = torch.tensor([2., 2., 2.])

# Task 3: Call the API
result = torch.divide(a, b)
print(result)
import torch

# Task 2: Generate input data
a = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([4.0, 5.0, 6.0])

# Task 3: Call the API
result = a.add_(other)
print(result)
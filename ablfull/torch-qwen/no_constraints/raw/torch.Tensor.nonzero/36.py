import torch

# Task 2: Generate input data
data = torch.tensor([[0, 1, 2], [3, 0, 5], [6, 7, 0]])

# Task 3: Call the API
result = data.nonzero()
print(result)
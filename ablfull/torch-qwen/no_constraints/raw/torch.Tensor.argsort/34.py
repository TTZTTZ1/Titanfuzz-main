import torch

# Task 2: Generate input data
data = torch.tensor([3, 1, 4, 1, 5, 9, 2])

# Task 3: Call the API
sorted_indices = data.argsort()

print(sorted_indices)
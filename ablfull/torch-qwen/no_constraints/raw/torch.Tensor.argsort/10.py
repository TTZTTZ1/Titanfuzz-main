import torch

# Task 2: Generate input data
data = torch.tensor([4, 1, 2, 8, 5])

# Task 3: Call the API
sorted_indices = data.argsort()

print(sorted_indices)
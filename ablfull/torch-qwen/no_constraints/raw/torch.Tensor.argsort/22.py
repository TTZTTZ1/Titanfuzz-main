import torch

# Task 2: Generate input data
data = torch.tensor([4, 3, 1, 2])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = data.argsort()

print(sorted_indices)
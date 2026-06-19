import torch

# Task 2: Generate input data
input_data = torch.tensor([4, 1, 2, 3])

# Task 3: Call the API
sorted_indices = input_data.argsort()

print(sorted_indices)
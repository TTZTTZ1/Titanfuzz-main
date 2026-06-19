import torch

# Task 2: Generate input data
input_tensor = torch.tensor([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = input_tensor.argsort()

print(sorted_indices)
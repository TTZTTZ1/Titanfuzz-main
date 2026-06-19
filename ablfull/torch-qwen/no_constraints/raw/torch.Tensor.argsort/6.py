import torch

# Task 2: Generate input data
input_tensor = torch.tensor([4, 1, 2, 3])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = input_tensor.argsort()

print(sorted_indices)
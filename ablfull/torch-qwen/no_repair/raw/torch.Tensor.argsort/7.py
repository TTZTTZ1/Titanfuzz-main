import torch

# Task 2: Generate input data
input_tensor = torch.tensor([3, 1, 4, 1, 5])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = input_tensor.argsort(dim=0, descending=False)
print(sorted_indices)
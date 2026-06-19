import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2, 3], [6, 5, 4]])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = input_tensor.argsort(dim=1, descending=False)
print(sorted_indices)
import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 0, 2], [3, 4, 5]])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = input_tensor.argsort(dim=1, descending=True)
print(sorted_indices)
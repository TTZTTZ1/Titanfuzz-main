import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[10, 50, 30], [60, 20, 40]])

# Task 3: Call the API torch.Tensor.argsort
sorted_indices = input_tensor.argsort(dim=1, descending=True)

print(sorted_indices)
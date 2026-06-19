import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[10, 5], [3, 8]])

# Task 3: Call the API
result = input_tensor.cummin(dim=1)

print(result)
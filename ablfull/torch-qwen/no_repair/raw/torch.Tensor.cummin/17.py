import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[10, 50], [30, 20]])

# Task 3: Call the API
result = input_tensor.cummin(dim=1)

print(result)
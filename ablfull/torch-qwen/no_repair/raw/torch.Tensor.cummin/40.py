import torch

# Task 2: Generate input data
input_data = torch.tensor([[1, 4, 3], [8, 5, 6]])

# Task 3: Call the API
result = input_data.cummin(dim=1)
print(result)
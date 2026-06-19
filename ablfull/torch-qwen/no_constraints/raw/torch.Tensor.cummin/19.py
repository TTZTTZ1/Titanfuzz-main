import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.int)

# Task 3: Call the API
result = input_tensor.cummin(dim=0)
print(result)
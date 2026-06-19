import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[4, 2], [1, 3]])

# Task 3: Call the API torch.Tensor.cummin
result = input_tensor.cummin(dim=0)

print(result)
import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Task 3: Call the API torch.Tensor.cummin
result = input_tensor.cummin(dim=1)

print(result)
import torch

# Task 2: Generate input data
input_tensor = torch.tensor([[10, 5], [3, 8]], dtype=torch.int)

# Task 3: Call the API
result = torch.Tensor.cummin(input_tensor, dim=0)
print(result)
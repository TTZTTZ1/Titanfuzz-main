import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 5)

# Task 3: Call the API torch.Tensor.stride
result = input_tensor.stride()

print(result)
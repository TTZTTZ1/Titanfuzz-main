import torch

# Task 2: Generate input data
input_tensor = torch.randn(10)
split_sizes = [4, 3, 3]

# Task 3: Call the API torch.Tensor.split
result = input_tensor.split(split_sizes, dim=0)

print(result)
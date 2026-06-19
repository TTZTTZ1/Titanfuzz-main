import torch

# Task 2: Generate input data
input_tensor = torch.randn(4, 5)

# Task 3: Call the API
split_result = input_tensor.split(split_size=[2, 2], dim=0)

print(split_result)
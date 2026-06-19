import torch

# Task 2: Generate input data
tensor = torch.randn(10)
split_size_or_number_of_splits = [2, 3, 5]

# Task 3: Call the API
result = tensor.split(split_size_or_number_of_splits)

print(result)
import torch

# Task 2: Generate input data
input_data = [1, 2, 3]

# Task 3: Call the API
result = torch.atleast_1d(*input_data)

print(result)
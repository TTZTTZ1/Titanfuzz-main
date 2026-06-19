import torch

# Task 2: Generate input data
input_data = 42  # A scalar value

# Task 3: Call the API
result = torch.atleast_1d(input_data)

print(result)
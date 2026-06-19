import torch

# Task 2: Generate input data - a tensor of booleans
input_data = torch.tensor([True, False, True])

# Task 3: Call the API torch.any
result = torch.any(input_data)

print(result)
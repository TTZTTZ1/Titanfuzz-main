import torch

# Task 2: Generate input data
input_data = torch.tensor([-float('inf'), 0., float('inf')])

# Task 3: Call the API
result = torch.isneginf(input_data)

print(result)
import torch

# Task 2: Generate input data
input_tensor = torch.tensor([-float('inf'), 0., float('inf')])

# Task 3: Call the API torch.isneginf
result = torch.isneginf(input_tensor)

print(result)
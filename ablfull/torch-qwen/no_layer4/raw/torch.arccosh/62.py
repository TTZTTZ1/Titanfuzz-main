import torch

# Task 2: Generate input data
input_data = torch.tensor([2.0, 4.0, 6.0], dtype=torch.float)

# Task 3: Call the API
result = torch.arccosh(input_data)
print(result)
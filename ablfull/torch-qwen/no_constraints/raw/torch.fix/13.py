import torch

# Task 2: Generate input data
input_data = torch.tensor([-1.5, 0.0, 1.5])

# Task 3: Call the API
result = torch.fix(input_data)

print(result)
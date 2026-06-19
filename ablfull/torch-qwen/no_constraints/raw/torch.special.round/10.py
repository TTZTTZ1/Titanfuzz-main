import torch

# Task 2: Generate input data
input_data = torch.tensor([-1.5, -0.4, 0.2, 1.7])

# Task 3: Call the API
result = torch.special.round(input_data)

print(result)
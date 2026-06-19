import torch

# Task 2: Generate input data
input_data = torch.tensor([-1.5, -0.5, 0.5, 1.5])

# Task 3: Call the API torch.special.round
result = torch.special.round(input_data)

print(result)
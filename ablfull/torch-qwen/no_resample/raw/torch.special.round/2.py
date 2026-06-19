import torch

# Task 2: Generate input data
input_data = torch.tensor([1.5, -2.3, 4.7], dtype=torch.float)

# Task 3: Call the API torch.special.round
result = torch.special.round(input_data)
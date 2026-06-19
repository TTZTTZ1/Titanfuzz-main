import torch

# Task 2: Generate input data
input_data = torch.tensor([0.25, 0.5, 0.75])

# Task 3: Call the API
result = torch.special.logit(input_data)
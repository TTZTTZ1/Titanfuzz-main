import torch

# Task 2: Generate input data
input_data = torch.tensor([0.5, 0.7, 0.3])

# Task 3: Call the API torch.special.logit
result = torch.special.logit(input_data)
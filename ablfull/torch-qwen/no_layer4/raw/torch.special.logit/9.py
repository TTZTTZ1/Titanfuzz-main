import torch

# Generate input data
input_data = torch.tensor([0.5, 0.7, 0.3], dtype=torch.float)

# Call the API
result = torch.special.logit(input_data)
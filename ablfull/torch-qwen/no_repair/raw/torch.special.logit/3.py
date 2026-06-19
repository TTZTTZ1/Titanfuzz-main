import torch

# Generate input data
input_data = torch.tensor([0.25, 0.75])

# Call the API
result = torch.special.logit(input_data)
import torch

# Generate input data
input_tensor = torch.tensor([0.1, 0.5, 0.9])

# Call the API
result = torch.special.logit(input_tensor)
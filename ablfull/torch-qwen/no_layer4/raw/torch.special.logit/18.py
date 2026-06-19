import torch

# Generate input data
input_tensor = torch.tensor([-0.5, 0.0, 0.5])

# Call the API
result = torch.special.logit(input_tensor)
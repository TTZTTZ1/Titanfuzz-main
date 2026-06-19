import torch

# Generate input data
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Call the API
result = torch.special.logit(input_tensor)
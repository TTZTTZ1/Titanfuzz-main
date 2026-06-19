import torch

# Generate input data
input_tensor = torch.tensor([0.5, 0.7, 0.3], dtype=torch.float)

# Call the API
result = torch.special.logit(input_tensor)
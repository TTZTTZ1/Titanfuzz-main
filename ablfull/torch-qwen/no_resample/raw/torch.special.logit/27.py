import torch

# Prepare input data
input_tensor = torch.tensor([0.1, 0.5, 0.9], dtype=torch.float)

# Call the API
result = torch.special.logit(input_tensor)
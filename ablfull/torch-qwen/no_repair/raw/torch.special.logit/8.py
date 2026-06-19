import torch

# Prepare valid input data
input_tensor = torch.tensor([0.5, 0.75, 0.9])

# Call the API
result = torch.special.logit(input_tensor)
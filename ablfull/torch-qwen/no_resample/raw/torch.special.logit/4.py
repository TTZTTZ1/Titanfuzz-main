import torch

# Prepare valid input data
input_tensor = torch.tensor([0.5, 0.7, 0.3])

# Call the API
result = torch.special.logit(input_tensor)
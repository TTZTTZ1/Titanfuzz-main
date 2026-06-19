import torch

# Prepare valid input data
input_tensor = torch.tensor([0.25, 0.75])

# Call the API
result = torch.special.logit(input_tensor)
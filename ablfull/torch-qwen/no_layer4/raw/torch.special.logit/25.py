import torch

# Prepare valid input data
input_data = torch.tensor([-1.0, 0.0, 1.0])

# Call the API with the prepared input data
result = torch.special.logit(input_data)
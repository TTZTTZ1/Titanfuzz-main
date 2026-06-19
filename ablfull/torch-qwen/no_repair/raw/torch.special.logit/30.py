import torch

# Prepare valid input data
input_data = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Call the API
result = torch.special.logit(input_data)
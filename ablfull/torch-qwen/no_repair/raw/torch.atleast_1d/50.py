import torch

# Prepare valid input data
input_tensor = torch.tensor(5)

# Call the API
result = torch.atleast_1d(input_tensor)
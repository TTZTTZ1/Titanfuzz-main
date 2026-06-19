import torch

# Prepare valid input data
input_tensor = torch.tensor([1, 2, 3])

# Call the target API
output = torch.atleast_1d(input_tensor)
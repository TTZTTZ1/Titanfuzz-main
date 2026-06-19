import torch

# Prepare valid input data
input_tensor = torch.tensor([-1.5, 0.5, 1.5])

# Call the API
result = torch.fix(input_tensor)
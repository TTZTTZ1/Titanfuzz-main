import torch

# Prepare valid input data
input_data = torch.tensor([-1.5, 0.3, 2.7])

# Call the API
result = torch.fix(input_data)
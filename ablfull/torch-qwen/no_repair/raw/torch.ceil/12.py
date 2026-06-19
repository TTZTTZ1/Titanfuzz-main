import torch

# Prepare valid input data
input_tensor = torch.tensor([-1.5, 0.3, 2.7], dtype=torch.float)

# Call the API
result = torch.ceil(input_tensor)
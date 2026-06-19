import torch

# Prepare valid input data
input_tensor = torch.tensor([-1.5, 0.3, 2.7], dtype=torch.float32)

# Call the API
result = torch.fix(input_tensor)
import torch

# Prepare valid input data
input_data = torch.tensor([0.5, 1.0, 2.0], dtype=torch.float32)

# Call the API with the prepared input data
result = torch.special.psi(input_data)
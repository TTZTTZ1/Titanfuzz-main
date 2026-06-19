import torch

# Prepare input data
input_data = torch.tensor([-0.5, 0.0, 0.5], dtype=torch.float32)

# Call the API
result = torch.special.psi(input_data)
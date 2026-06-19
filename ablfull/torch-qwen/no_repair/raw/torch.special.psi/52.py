import torch

# Generate input data
input_data = torch.tensor([0.5, 1.5, 2.5], dtype=torch.float32)

# Call the API
result = torch.special.psi(input_data)
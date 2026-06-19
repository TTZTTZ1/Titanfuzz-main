import torch

# Generate input data
input_data = torch.tensor([-2.0, -1.5, 0.0, 0.5, 1.0], dtype=torch.float32)

# Call the API
result = torch.special.psi(input_data)
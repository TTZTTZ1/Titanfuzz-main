import torch

# Generate input data
input_data = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Call the API
result = torch.special.psi(input_data)
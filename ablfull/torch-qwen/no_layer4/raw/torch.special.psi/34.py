import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.5, 3.7], dtype=torch.float32)

# Call the API
result = torch.special.psi(input_tensor)
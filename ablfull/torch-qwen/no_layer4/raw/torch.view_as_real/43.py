import torch

# Generate input data
input_tensor = torch.tensor([1+2j, 3+4j], dtype=torch.complex64)

# Call the API
result = torch.view_as_real(input_tensor)
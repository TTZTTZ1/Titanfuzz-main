import torch

# Generate input data
input_data = torch.tensor([[1+2j, 3+4j], [5+6j, 7+8j]], dtype=torch.complex64)

# Call the API
result = torch.view_as_real(input_data)
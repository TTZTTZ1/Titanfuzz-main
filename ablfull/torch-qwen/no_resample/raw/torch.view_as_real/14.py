import torch

# Generate complex input data
input_data = torch.tensor([1+2j, 3+4j], dtype=torch.complex64)

# Call torch.view_as_real
result = torch.view_as_real(input_data)
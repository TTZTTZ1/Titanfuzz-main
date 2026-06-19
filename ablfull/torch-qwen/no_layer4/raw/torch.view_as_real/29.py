import torch

# Generate complex input tensor
input_tensor = torch.tensor([1+2j, 3+4j], dtype=torch.complex64)

# Call torch.view_as_real
output = torch.view_as_real(input_tensor)
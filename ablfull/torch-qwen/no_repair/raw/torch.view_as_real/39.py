import torch

# Generate complex tensor input
input_tensor = torch.tensor([[1+2j, 3+4j], [5+6j, 7+8j]], dtype=torch.complex64)

# Call torch.view_as_real
result = torch.view_as_real(input_tensor)
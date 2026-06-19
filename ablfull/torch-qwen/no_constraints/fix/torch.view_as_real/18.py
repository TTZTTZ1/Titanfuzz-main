import torch
input_data = torch.randn(4, 4, dtype=torch.complex64)
output_data = torch.view_as_real(input_data)
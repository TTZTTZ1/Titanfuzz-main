import torch
input_data = torch.randn(4, 5, dtype=torch.complex64)
result = torch.view_as_real(input_data)
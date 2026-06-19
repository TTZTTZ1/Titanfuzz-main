import torch
input_tensor = torch.randn(4, 4, dtype=torch.complex64)
result = torch.view_as_real(input_tensor)
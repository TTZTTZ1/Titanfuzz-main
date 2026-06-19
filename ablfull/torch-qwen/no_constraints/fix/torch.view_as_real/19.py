import torch
input_data = torch.complex(torch.randn(4), torch.randn(4))
result = torch.view_as_real(input_data)
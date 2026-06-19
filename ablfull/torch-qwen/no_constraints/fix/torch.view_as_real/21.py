import torch
input_data = torch.complex(torch.rand(4), torch.rand(4))
result = torch.view_as_real(input_data)
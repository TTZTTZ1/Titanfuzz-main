import torch
input_tensor = torch.complex(torch.rand(4), torch.rand(4))
output_tensor = torch.view_as_real(input_tensor)
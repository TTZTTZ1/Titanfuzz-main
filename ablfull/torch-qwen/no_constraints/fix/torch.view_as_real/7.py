import torch
input_data = torch.complex(torch.arange(8, dtype=torch.float32), torch.arange(8, dtype=torch.float32))
output_data = torch.view_as_real(input_data)
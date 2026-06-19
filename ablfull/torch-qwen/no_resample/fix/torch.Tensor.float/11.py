import torch
input_data = torch.randn(3, 4, 5)
output_data = input_data.float(memory_format=torch.contiguous_format)
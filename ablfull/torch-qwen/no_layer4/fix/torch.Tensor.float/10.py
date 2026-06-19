import torch
input_data = torch.randn(4, 4)
output_data = input_data.float(memory_format=torch.preserve_format)
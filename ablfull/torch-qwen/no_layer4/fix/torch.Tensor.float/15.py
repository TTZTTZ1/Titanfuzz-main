import torch
input_data = torch.randn(5, 5)
output = input_data.float(memory_format=torch.preserve_format)
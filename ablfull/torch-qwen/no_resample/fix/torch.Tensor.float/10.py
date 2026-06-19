import torch
input_data = torch.randn(3, 4)
output_tensor = input_data.float(memory_format=torch.preserve_format)
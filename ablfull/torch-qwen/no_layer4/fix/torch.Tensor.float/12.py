import torch
input_data = torch.randn(3, 3)
result = input_data.float(memory_format=torch.preserve_format)
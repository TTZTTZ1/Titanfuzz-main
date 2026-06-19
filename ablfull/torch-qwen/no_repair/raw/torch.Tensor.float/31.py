import torch

input_data = torch.randn(4, 4)
result = input_data.float(memory_format=torch.preserve_format)
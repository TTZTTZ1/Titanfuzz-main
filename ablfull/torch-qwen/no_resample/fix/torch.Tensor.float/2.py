import torch
input_data = torch.randn(1, 3, 4, 4)
result = input_data.float(memory_format=torch.channels_last)
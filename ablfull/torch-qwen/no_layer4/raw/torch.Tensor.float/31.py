import torch

input_data = torch.randn(4, 4)
output = input_data.float(memory_format=torch.channels_last)
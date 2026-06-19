import torch

input_tensor = torch.randn(3, 4)
output_tensor = input_tensor.float(memory_format=torch.channels_last)
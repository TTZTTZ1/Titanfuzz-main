import torch
input_tensor = torch.randn(1, 3, 4, 4)
output_tensor = input_tensor.float(memory_format=torch.channels_last)
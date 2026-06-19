import torch
input_tensor = torch.randn(1, 3, 4, 5)
output_tensor = input_tensor.float(memory_format=torch.channels_last)
import torch

input_tensor = torch.randint(0, 256, (3, 4, 5))
output_tensor = input_tensor.float(memory_format=torch.channels_last)
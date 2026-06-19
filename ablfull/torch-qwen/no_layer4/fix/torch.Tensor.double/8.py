import torch
input_tensor = torch.randn(3, 4)
output_tensor = input_tensor.double(memory_format=torch.preserve_format)
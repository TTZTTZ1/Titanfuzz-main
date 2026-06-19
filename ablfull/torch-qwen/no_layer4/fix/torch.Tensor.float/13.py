import torch
input_tensor = torch.randn(3, 4, 5)
output_tensor = input_tensor.float(memory_format=torch.preserve_format)
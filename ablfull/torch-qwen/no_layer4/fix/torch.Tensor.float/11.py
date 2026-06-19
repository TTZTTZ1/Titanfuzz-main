import torch
input_tensor = torch.randn(5)
result = input_tensor.float(memory_format=torch.preserve_format)
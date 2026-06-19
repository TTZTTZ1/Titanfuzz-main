import torch
input_tensor = torch.randn(3, 4, device='cpu')
output_tensor = input_tensor.float(memory_format=torch.contiguous_format)
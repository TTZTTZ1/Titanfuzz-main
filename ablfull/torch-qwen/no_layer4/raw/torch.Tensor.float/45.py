import torch

input_tensor = torch.randn(5, requires_grad=True)
output_tensor = input_tensor.float(memory_format="contiguous_format")
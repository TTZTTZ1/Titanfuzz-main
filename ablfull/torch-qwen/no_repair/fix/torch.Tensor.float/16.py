
import torch
input_tensor = torch.randn(3, requires_grad=True)
output_tensor = input_tensor.float(memory_format=torch.preserve_format)

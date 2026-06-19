
import torch
input_tensor = torch.randn(4, 4)
output_tensor = input_tensor.float(memory_format=torch.preserve_format)

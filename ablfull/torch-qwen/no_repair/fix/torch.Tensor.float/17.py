
import torch
input_tensor = torch.rand(4, 5)
output_tensor = input_tensor.float(memory_format=torch.contiguous_format)
